# Engineering Log

## 2026-05-16 - Analysis checkpoint
- Scope: Reviewed the project management automation stack for portfolio extraction.
- Findings: the module combines global attendance gating, geofenced check-in, dependency/attachment/feedback close rules, Documents folder orchestration, and session history persistence.
- Impact signal: strongest reusable story is a policy-enforced ERP workflow that blocks premature task closure and centralizes check-in evidence in hr.attendance plus mobipine_project.checkin_session.

## 2026-04-24 - Attendance-Backed Check-in Slice
- Scope: Started replacing the custom project-only session entry with an attendance-backed check-in wizard, global open-session tracking, partner geofence fields, and SLA function drill-down UI.
- Files changed: manifest dependency/data list, root init import, new hr_employee model hook, expanded check-in session model, partner fields/view, project/task session logic, project and HR function views, and new attendance check-in wizard files.
- Data flow changes: attendance check-in now creates an hr.attendance row plus a linked mobipine_project.checkin_session history row; checkout closes both records; project/task session guards now look for a global open session by user.
- Fixes applied: added client radius/location fields on res.partner, raised the default radius to 30 km with a post-init backfill, and surfaced SLA HR functions on the project form with a task-count smart button on HR functions.
- Verification: Python and XML load checks passed for the edited files; backend geolocation capture widget is now wired into the attendance wizard; partner coordinates now reuse the standard industry_fsm/partner_latitude/partner_longitude fields; duplicate project/task check-in buttons were removed so Attendance is the single check-in path.

## 2026-04-21 - Phase 1 Foundation Bootstrap
- Scope: Created Phase 1 foundation for StellarHR project module including SLA structures, HR function templates, recurring task spawn skeleton, security baseline, and setup views.
- Files changed: module manifest/init, 7 model files, security XML/CSV, data XML, and core views/menus.
- Data flow changes: project.task records can now be generated from mobipine_project.task_template via daily cron, keyed by project + template + cycle date.
- Fixes applied: removed fragile kanban inherited view; aligned SLA security rule with company scope by adding company_id on SLA model.
- Verification: module upgrade command completed successfully in Odoo 19 container using database postgres.

## 2026-04-22 - V2 Phase 1 Folder Hierarchy Start
- Scope: Implemented document folder hierarchy for project tasks and subtasks with task-level smart button navigation and upload destination routing.
- Files changed: manifest dependencies, models init, project_task model extension, new ir_attachment extension, and new task documents view.
- Data flow changes: task/subtask creation now auto-creates a Documents folder linked on task; chatter upload destination for project.task now prefers task folder, then project folder fallback.
- Fixes applied: aligned implementation with Odoo 19 Documents architecture using documents.document folders (type=folder) and documents_project integration rather than a non-existent documents.folder model.
- Verification: module upgrade completed successfully with mobipine_odoo_project_management on postgres; no registry traceback.

## 2026-04-22 - V2 Phase 2 Session Gate + Naming Cleanup
- Scope: Implemented check-in session model, project check-in/out actions, task write guard enforcement, session views/menus, and removed Mobipine prefixes from class names and file names in core model/view files.
- Files changed: manifest data paths, model imports, renamed model/view files, new project_checkin_session model and views, project_project/session actions, project_task session guard, security ACL/rule updates.
- Data flow changes: associates must have an open project session before project.task.write is allowed; PM/Admin bypass is preserved.
- Fixes applied: session ownership and single-open-session-per-user-per-project constraint logic added with close-session action and duration computation.
- Verification: module upgrade command completed successfully in Odoo 19 container with no registry errors.

## 2026-04-22 - Odoo 19 View Type + Menu Anchoring Fix
- Scope: Fixed remaining action view modes using tree and re-anchored module menus under native Projects.
- Files changed: project_hr_function_views.xml, project_checkin_session_views.xml, menu_views.xml, __manifest__.py.
- Data flow changes: none; navigation and action compatibility only.
- Fixes applied: changed action view_mode to list,form and set menu root parent to project.menu_main_pm; set module application flag to False.
- Verification: pending immediate upgrade validation in container.

## 2026-04-22 - Session UX Decisions Implemented
- Scope: Applied confirmed session rules and mirrored check-in/check-out controls across project and task contexts.
- Files changed: project_checkin_session.py, project_project.py, project_task.py, project_task_views.xml.
- Data flow changes: one open session globally per user; task create and core task field edits require an open session; chatter/doc-style non-core updates are allowed.
- Fixes applied: previous menu/action regression revalidated in vivace_test (action ids 719 and 721 now list,form; StellarHR menu parent is Project).
- Verification: module upgrade successful on vivace_test after changes.
## April 22, 2026 - StellaHR V2 Implementation (Phases 1-4)
**Decisions**:
- Cleaned up duplicated models `mobipine_project_sla.py`, `mobipine_project_hr_function.py`, `mobipine_project_task_template.py` to prevent registry conflicts.
- Applied patch to implement missing logic for Sections 2.1-2.4 of system design.
- Features implemented: Auto-create HR stubs, task dependencies, feedback constraints, soft-delete rules for folders, geo-location capture, and session-based read-only gate.

**Data Flow**:
- Check-in `session_gate` (OWL JS) intercepts the UI fields based on active `.checkin_session`.
- SLA modifications auto-trigger HR function creation to match the templates.
- Task closure intercepts through `parent_task_ids` constraint logic.

**Errors / Fixes**:
- Erroneous directory creation during the patch generation (`mobipine_odoo_project_management` at root). Copied and merged appropriately to `custom_addons/` path.
## 2026-04-22 Registry recovery pass
- Root cause 1: missing DB column `ir_attachment.doc_type_id` after model change; resolved by module upgrade command.
- Root cause 2: `project_project.py` was truncated and lost session compute fields/methods used by views.
- Root cause 3: `project_task.py` lacked object methods used by view buttons (`action_check_in`, `action_check_out`, `action_view_task_documents`) and missing session compute fields.
- Root cause 4: manifest referenced missing `views/stellar_document_type_views.xml`.
- Fix commands: `docker compose exec odoo19 odoo -c /etc/odoo/odoo.conf -d vivace_test -u mobipine_odoo_project_management --stop-after-init`.
- Outcome: module upgrade completed; registry loaded cleanly.
## 2026-04-22 Frontend blank screen/debug toggle incident
- Symptom: after module install, Apps vanished and page rendered gray; URL showed `debug=0`.
- Root cause: broken custom backend JS asset (`geolocation.js` contained invalid JS triple-quote syntax), likely crashing bundled web assets.
- Fix: removed custom files from `web.assets_backend` in manifest and replaced JS files with no-op safe modules.
- Validation: module upgrade completed and registry loaded successfully after change.
