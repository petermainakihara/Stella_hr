# Concepts

## 2026-05-16 - Portfolio Extraction Notes
- The project module is a control-plane for services delivery: it gates access, enforces task close criteria, captures geolocation, and persists audit history.
- One open session per user is the effective operating model; the system intentionally fails closed for associates but preserves PM/Admin bypass.
- Task completion is only allowed when dependencies, required attachments, and feedback are satisfied, which makes the module suitable for SLA-style work rather than generic task tracking.

## Attendance-Backed Check-in Slice
- Odoo Attendance is now the check-in source of truth; the custom session table is used as the audit/history layer.
- Check-in history stores the linked attendance record, selected client, notes, check-in coordinates, radius, and distance check.
- Project and task session lookups now treat an open session as global per user instead of project-scoped.
- The project form now shows an SLA functions tab for the primary SLA, and each HR function exposes a task smart button.
- Browser geolocation capture is wired through a backend field widget that fills the wizard coordinates on mount.
- Partner coordinates are reused from Odoo's standard Field Service/partner_latitude/partner_longitude fields; the project module only adds the check-in radius.
- The partner radius default is 30 km, and existing partners are backfilled to that value on upgrade.
- Attendance is the only check-in entry point; duplicate project/task check-in buttons are removed.

## Phase 1 Design Decisions
- Model namespace uses mobipine_project.* as requested, while module technical name remains mobipine_odoo_project_management.
- Foundation phase prioritizes setup entities and orchestration metadata over execution controls.
- Recurrence ownership lives on task templates to support mixed frequencies in a single SLA.
- Cron idempotency is enforced through a unique task key: project_id + task_template_id + cycle_date.
- Sensitive client/SLA setup fields are restricted to PM/Admin group scope in this phase.

## Deferred to Later Phases
- Dependency gating before task completion.
- Attachment and feedback completion gates.
- Geo check-in/offsite capture flow.
- Shift accountability analytics and final report template outputs.

## V2 Folder Hierarchy Concepts
- Odoo 19 folder records are documents.document entries with type="folder"; folder nesting is driven by folder_id.
- Project workspace linkage should reuse documents_project native field documents_folder_id on project.project.
- Task and subtask folder linkage is handled by documents_folder_id on project.task.
- Folder ancestry rule: subtask folder parent is parent task folder when available; otherwise project documents folder.
- Smart-button document counts should include descendants using child_of on folder id for complete subtree visibility.

## V2 Session Gate Concepts
- Session model is user-scoped globally: one open session per user across all projects.
- Entry points are project actions (Check In / Check Out), not task-level check-in.
- Enforcement layer is ORM-first by guarding project.task.create and core project.task.write fields for non-PM/non-admin users.
- Non-core collaboration updates (for example chatter and document flows) remain allowed without forcing a session.
- Project form header remains primary trigger; task list and task form expose mirrored check-in/check-out triggers that call the same project session actions.

## Navigation and App Positioning
- Module should behave as an extension of Project (and related HR flows), not as a standalone app.
- Custom menus are anchored under native Project menu hierarchy to preserve user mental model.
- Odoo 19 action entries should use list,form view modes (tree is rejected in this environment).

## Naming Cleanup
- Python class names now use neutral naming (ProjectSLA, ProjectHRFunction, ProjectTaskTemplate, ProjectSpawnLog).
- File naming moved to neutral style (project_sla.py, project_hr_function.py, project_task_template.py, project_spawn_log.py and matching view filenames).

## Odoo Decorators and API Reference

This section documents the most important Odoo backend decorators, recordset helpers, and commonly imported utilities used when building business logic.

### 1) @api.model
Use for model-level methods where incoming data is not tied to one specific record.

```python
from odoo import api, models


class ProjectTask(models.Model):
	_inherit = "project.task"

	@api.model
	def find_open_tasks(self):
		return self.search([("stage_id.fold", "=", False)])
```

How it works:
- `self` is still a model recordset, but this method is conceptually model-scoped.
- Common for helpers, cron entry points, and service methods.

### 2) @api.model_create_multi
Use when overriding `create` so Odoo can create multiple records efficiently in one call.

```python
from odoo import api, fields, models


class ProjectSLA(models.Model):
	_name = "mobipine_project.sla"

	name = fields.Char(required=True)
	code = fields.Char(default="New", copy=False, readonly=True)

	@api.model_create_multi
	def create(self, vals_list):
		seq = self.env["ir.sequence"]
		for vals in vals_list:
			if vals.get("code", "New") == "New":
				vals["code"] = seq.next_by_code("mobipine_project.sla") or "New"
		return super().create(vals_list)
```

How it works:
- Receives a list of dictionaries.
- Must return a recordset of created records.
- Better performance than forcing one-by-one create calls.

### 3) @api.depends
Declares field dependencies for computed fields.

```python
from odoo import api, fields, models


class CheckinSession(models.Model):
	_name = "mobipine_project.checkin_session"

	check_in_time = fields.Datetime()
	check_out_time = fields.Datetime()
	duration_hours = fields.Float(compute="_compute_duration_hours", store=True)

	@api.depends("check_in_time", "check_out_time")
	def _compute_duration_hours(self):
		for rec in self:
			if rec.check_in_time and rec.check_out_time:
				rec.duration_hours = (rec.check_out_time - rec.check_in_time).total_seconds() / 3600.0
			else:
				rec.duration_hours = 0.0
```

How it works:
- Odoo recomputes the field when any listed dependency changes.
- Use `store=True` if field should be searchable and persisted.

### 4) @api.depends_context
Adds context keys as dependencies for computed fields.

```python
from odoo import api, fields, models


class ResPartner(models.Model):
	_inherit = "res.partner"

	display_label = fields.Char(compute="_compute_display_label")

	@api.depends_context("lang", "uid")
	def _compute_display_label(self):
		for rec in self:
			rec.display_label = rec.with_context(lang=self.env.lang).display_name
```

How it works:
- Recompute behavior depends on context changes, not just field changes.

### 5) @api.constrains
Runs server-side validation after create/write for the specified fields.

```python
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProjectProject(models.Model):
	_inherit = "project.project"

	shift_start = fields.Float(default=8.0)
	shift_end = fields.Float(default=16.0)

	@api.constrains("shift_start", "shift_end")
	def _check_shift_window(self):
		for rec in self:
			if rec.shift_end <= rec.shift_start:
				raise ValidationError("Shift end must be greater than shift start.")
```

How it works:
- Rejects invalid data at ORM level.
- Must raise `ValidationError` when invalid.

### 6) @api.onchange
Client-form helper: updates transient values in UI before save.

```python
from odoo import api, fields, models


class ProjectProject(models.Model):
	_inherit = "project.project"

	client_partner_id = fields.Many2one("res.partner")
	partner_id = fields.Many2one("res.partner")

	@api.onchange("client_partner_id")
	def _onchange_client_partner_id(self):
		for rec in self:
			if rec.client_partner_id:
				rec.partner_id = rec.client_partner_id
```

How it works:
- Runs only in form context.
- Does not enforce rules for RPC/import writes. Use constraints or write guards for hard validation.

### 7) @api.ondelete
Defines delete-time guard logic.

```python
from odoo import api, models
from odoo.exceptions import UserError


class ProjectSLA(models.Model):
	_name = "mobipine_project.sla"

	@api.ondelete(at_uninstall=False)
	def _unlink_except_unused(self):
		for rec in self:
			if rec.hr_function_ids:
				raise UserError("Cannot delete SLA with linked HR functions.")
```

How it works:
- Triggered during `unlink`.
- `at_uninstall=False` avoids uninstall deadlocks.

### 8) @api.returns
Specifies return model for compatibility and RPC behavior.

```python
from odoo import api, models


class ProjectTask(models.Model):
	_inherit = "project.task"

	@api.returns("project.task")
	def get_related_tasks(self):
		return self.search([("project_id", "in", self.mapped("project_id").ids)])
```

How it works:
- Useful for methods returning recordsets, especially when inherited/extended.

### 9) @api.autovacuum
Marks method for automatic periodic cleanup by Odoo vacuum job.

```python
from odoo import api, fields, models


class ProjectCheckinSession(models.Model):
	_name = "mobipine_project.checkin_session"

	state = fields.Selection([("open", "Open"), ("closed", "Closed")])
	check_out_time = fields.Datetime()

	@api.autovacuum
	def _gc_old_closed_sessions(self):
		old_sessions = self.search([
			("state", "=", "closed"),
			("check_out_time", "<", fields.Datetime.now()),
		])
		return len(old_sessions)
```

How it works:
- Intended for lightweight cleanup tasks.

## Recordset Helpers and Core Methods

### ensure_one()
Use when method logic expects exactly one record.

```python
def action_check_out(self):
	self.ensure_one()
	# safe single-record logic
```

### exists()
Filters out deleted/non-existing records.

```python
task = self.env["project.task"].browse(task_id)
if not task.exists():
	return False
```

### filtered()
Python-level filter on recordsets.

```python
open_tasks = self.filtered(lambda t: not t.stage_id.fold)
```

### mapped()
Extracts field values or chained relations.

```python
project_ids = self.mapped("project_id").ids
partner_names = self.mapped("partner_id.name")
```

### sorted()
Sorts recordsets in Python.

```python
ordered = self.sorted(key=lambda r: r.create_date or fields.Datetime.now())
```

### sudo()
Bypasses access rights and record rules.

```python
folder = self.env["documents.document"].sudo().create({"name": "Folder", "type": "folder"})
```

Guideline:
- Use only where needed and keep scope narrow.

### with_context()
Passes flags/data through context chain.

```python
self.with_context(skip_session_guard=True).write({"state": "done"})
```

### with_user()
Executes logic as another user.

```python
self.with_user(self.env.ref("base.user_admin")).action_confirm()
```

### with_company()
For multi-company-safe operations.

```python
self.with_company(target_company).create({"name": "Cross-company setup"})
```

### search(), browse(), create(), write(), unlink(), copy()
Core ORM CRUD operations.

```python
records = self.search([("active", "=", True)], limit=50)
record = self.browse(record_id)
new_record = self.create({"name": "New"})
records.write({"active": False})
records.unlink()
clone = new_record.copy({"name": "Copy"})
```

## Frequently Used Imports and Utilities

### Exceptions

```python
from odoo.exceptions import UserError, ValidationError, AccessError, MissingError
```

When to use:
- `ValidationError`: invalid business data.
- `UserError`: user-action feedback or blocked flow.
- `AccessError`: permission/session/role denial.
- `MissingError`: record missing in expected flow.

### Date/Datetime helpers

```python
today = fields.Date.context_today(self)
now = fields.Datetime.now()
```

### Translation helper

```python
from odoo import _

raise UserError(_("You must check in before updating tasks."))
```

### Command helper for x2many updates

```python
from odoo import Command

vals = {
	"partner_ids": [
		Command.clear(),
		Command.link(partner_id),
		Command.create({"name": "Inline Partner"}),
	]
}
record.write(vals)
```

Common commands:
- `Command.create(vals)`
- `Command.update(id, vals)`
- `Command.delete(id)`
- `Command.unlink(id)`
- `Command.link(id)`
- `Command.clear()`
- `Command.set([ids])`

## Practical Guard Pattern (Session-based Example)

```python
from odoo.exceptions import AccessError


def _check_session_guard(self):
	user = self.env.user
	if user.has_group("mobipine_odoo_project_management.group_project_manager") or user.has_group("base.group_system"):
		return

	projects = self.mapped("project_id")
	if not projects:
		return

	open_sessions = self.env["mobipine_project.checkin_session"].search([
		("user_id", "=", user.id),
		("state", "=", "open"),
		("project_id", "in", projects.ids),
	])
	allowed_project_ids = set(open_sessions.mapped("project_id").ids)
	blocked = projects.filtered(lambda p: p.id not in allowed_project_ids)
	if blocked:
		raise AccessError("Check in to the project before updating tasks.")
```

Why this pattern works:
- Enforces security at ORM level.
- Keeps privileged users operational.
- Works for UI and non-UI writes.
**Session Gate**
- OWL Component logic intercepting forms on UI level to toggle readonly attributes iteratively based on backend session data.

**Attachment Requirements**
- Constraints during task write validating if actual bound files matched template config.
## 2026-04-22 Recovery concepts
- View-Model contract in Odoo is strict: every object button `name` in XML must map to a model method at load time.
- Schema drift after adding stored fields (e.g., Many2one on `ir.attachment`) causes runtime SQL errors until module upgrade applies DDL.
- Prefer additive recovery: restore missing model methods/fields first, then rerun upgrade to surface the next deterministic parse error.
## 2026-04-22 Frontend stability concept
- In Odoo, one invalid JS module included in `web.assets_backend` can break the whole webclient and mimic unrelated issues (missing apps, debug toggles failing).
- During stabilization, prefer disabling risky assets in manifest and re-introduce them only after isolated testing.
