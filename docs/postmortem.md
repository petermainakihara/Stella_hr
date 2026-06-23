# Postmortem

## 2026-05-16 - Analysis checkpoint
- Observation: the implementation has matured from setup scaffolding into a policy-heavy workflow engine.
- Risk to watch: the strongest logic depends on browser geolocation, attendance state, and menu caching, so UAT must confirm reload behavior on real devices.
- Validation note: the close gate is intentionally strict; if any dependency, attachment, or feedback is missing, the task stays open.

## 2026-04-24 - Attendance-Backed Check-in Slice
- Issue: Attendance-driven check-in needed a geofenced wizard, session history persistence, and project UI hooks without keeping a second project-only session source of truth.
- Root cause: the existing implementation only tracked project-scoped sessions and had no attendance wizard, partner radius fields, or HR-function drill-down on the project form.
- Fix applied: added an attendance-backed wizard and hr.employee hook, linked sessions to hr.attendance, reused standard Field Service partner coordinates, added a 30 km project check-in radius with upgrade backfill, removed duplicate project/task check-in buttons, and surfaced SLA functions/task counts in the project UI.
- Remaining risk: the geolocation widget now auto-fills coordinates, but browser permission/HTTPS behavior still needs real-device UAT.
- Validation outcome: edited Python and XML files passed workspace error checks after the patch set.

## 2026-04-21 - Phase 1 Foundation Checkpoint
- Issue: Potential install-time failure from record rule domain referencing company scope on SLA without guaranteed company field.
- Root cause: initial SLA model definition omitted explicit company_id while rule used company-based domain filtering.
- Fix applied: added company_id to SLA model and adjusted SQL uniqueness to code + company.
- Remaining risk: external view IDs in project module can differ across distributions; only stable form inheritance was retained for this phase.
- Validation outcome: Odoo module update completed without traceback or model load errors.

## 2026-04-22 - V2 Folder Hierarchy Checkpoint
- Issue: V2 document references documents.folder, but Odoo 19 enterprise implementation uses documents.document for both files and folders.
- Root cause: cross-version design assumption from earlier documentation differed from live Odoo 19 data model.
- Fix applied: implemented folder hierarchy against documents.document (type=folder) and added documents_project dependency to reuse native project folder integration.
- Remaining risk: task folder access mirroring to project membership needs explicit UAT validation across multi-user projects.
- Validation outcome: module update completed successfully; no compile or registry errors.

## 2026-04-22 - V2 Session Gate + Naming Cleanup Checkpoint
- Issue: Need to enforce session gate without blocking PM/Admin workflows and background/system operations.
- Root cause: session policy applies to associates only; blanket write blocking would affect privileged flows.
- Fix applied: task write guard now bypasses for group_project_manager, base.group_system, and sudo contexts; associates require an open session per project.
- Remaining risk: UI-level readonly parity is not yet implemented with OWL component, so users only see enforcement on write actions in this checkpoint.
- Validation outcome: module upgrade passed after ACL/rule/view updates and class/file renaming changes.

## 2026-04-22 - Action View Type Regression
- Issue: frontend crash on menu open with "View types not defined tree" for HR Functions and Check-in Sessions.
- Root cause: two act_window records still had view_mode=tree,form after partial migration.
- Fix applied: migrated both actions to list,form and re-anchored menus under project.menu_main_pm to keep extension behavior.
- Remaining risk: browser may hold stale assets/action cache until hard refresh.
- Validation outcome: pending immediate upgrade + menu retest.

## 2026-04-22 - Session Policy Finalization
- Issue: session policy ambiguity (project-scoped vs user-global) and over-blocking task updates.
- Root cause: initial implementation enforced per-project open session and blocked broad task writes.
- Fix applied: switched to one global open session per user; task guard now blocks create and core task edits only, while allowing non-core collaboration flows.
- Remaining risk: task-list header buttons depend on selected rows and are not a full reactive status chip implementation.
- Validation outcome: vivace_test upgrade succeeded; action 719/721 are list,form and menu parent resolves under Project.
### StellaHR Project Management - Implementation 2.1 to 2.4
- **Successes**: Identified system duplicates quickly. Auto generation of a patch script cleanly implemented multiple models like feedback, attachment_req, etc.
- **Failures**: The external bash logic built the module in `Base Path` instead of `custom_addons`.
- **Mitigation**: Verified destination folder structures manually and executed bash copies to relocate the files correctly.
## 2026-04-22 Incident: registry load failures
- Symptom chain:
  1. `UndefinedColumn: ir_attachment.doc_type_id`
  2. ParseError on missing project method `action_view_checkin_sessions`
  3. ParseError on missing task methods `action_check_in/out`
  4. FileNotFound for `views/stellar_document_type_views.xml`
- Why it happened: previous automated patch left partial/truncated Python files and manifest references without corresponding XML file.
- Mitigation applied: restored model methods/compute fields, created missing XML view file, reran module upgrade until registry succeeded.
- Preventive action: run `-u mobipine_odoo_project_management --stop-after-init` after every structural patch before restarting HTTP workers.
## 2026-04-22 Webclient blank page after install
- Trigger: custom backend asset bundle included syntactically invalid JS.
- Impact: Odoo UI rendered gray/empty and appeared as if Apps disappeared; debug extension changes were ineffective.
- Resolution: asset isolation (manifest assets disabled) + module upgrade.
- Prevention: lint and smoke-test custom JS modules before adding to `web.assets_backend`.
