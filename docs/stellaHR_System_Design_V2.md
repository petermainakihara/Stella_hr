```
VERSION 1.
April 2026 — Rev 1
```
SYSTEM DESIGN DOCUMENT

# StellarHR

## Custom Odoo Module

## Built on project.task — Full System Design

```
Rev 1 changes: Document folder hierarchy · Session-based check-in gate · Document type on upload
```
```
DOCUMENT METADATA
Client Stella HR Solutions
Consultant MobiPine Limited
Prepared by Wycliff Ochieng
Document Version 1.1.
Date April 2026
Classification Confidential
```
mobipine.com | info@mobipine.com | +254 790 619 043 Imagine. Innovate. Inspire.


### TABLE OF CONTENTS

#### 1. Introduction & Scope

#### 1.1 Project Background

#### 1.2 Objectives

#### 1.3 Scope Boundaries

#### 1.4 Revision History

#### 2. Functional Requirements

#### 2.1 Client & SLA Management

#### 2.2 HR Function & Task Orchestration

#### 2.3 Document Folder Hierarchy H

#### 2.4 Session-Based Check-In Gate H

#### 2.5 Document Type on Upload H

#### 2.6 Onsite & Offsite Execution

#### 2.7 Role & Permission Model

#### 2.8 Reporting & Exports

#### 3. Non-Functional Requirements

#### 4. High-Level Design

#### 4.1 System Architecture

#### 4.2 Module Boundaries

#### 4.3 Integration Points

#### 5. Low-Level Design

#### 5.1 Data Model Overview

#### 5.2 Custom Models Reference H

#### 5.3 Business Logic H

#### 5.4 Security Rules

#### 5.5 API Surface

#### 6. Decisions & Trade-offs

#### 7. Implementation Roadmap

#### 8. Glossary

H Sections marked with H contain content revised in v1.


### 1 INTRODUCTION & SCOPE

#### 1.1 Project Background

#### Stella HR Solutions is an outsourced HR service provider operating in Kenya, serving both one-off and retainer

#### clients under defined Service Level Agreements (SLAs). MobiPine Limited has been engaged to implement an

#### Odoo 17 HR & Payroll platform, augmented by a bespoke custom module — stellar_hr — that extends the

#### native project.task model to support StellarHR's unique operational model: SLA-driven recurring HR

#### functions, session-gated task execution, structured document folder hierarchies, typed file uploads, geo-tracked

#### attendance, and hierarchical client reporting.

#### 1.2 Objectives

- Map each client SLA to a defined set of HR functions, each containing dependent task templates.
- Automatically spawn recurring tasks for retainer clients on a configurable schedule.
- Auto-create a three-level folder hierarchy (Project → Task → Subtask) in the Odoo Documents module

#### for every record.

- Enforce a session-based check-in gate: tasks and subtasks are read-only until an associate opens a

#### session for that project.

- Require a Document Type classification on every file uploaded — selected from a system-wide

#### configured list.

- Enforce Project Manager-only task assignment with real-time assignee notifications.
- Capture GPS coordinates for offsite task execution; require physical check-in for onsite projects.
- Gate task completion on required file attachments and assignee feedback submission.
- Provide a hierarchical reporting view: Client Project → HR Function → Task (with progress).
- Support Day/Night shift scheduling with 8-hour cycle accountability.

#### 1.3 Scope Boundaries

```
IN SCOPE stellar_hr custom module; extensions to project.project, project.task, res.partner, ir.attachment,
documents.folder; session-based check-in gate; document folder auto-creation; document type
classification; geo-location capture; shift scheduling; SLA-task engine; role-gated assignment;
hierarchical reporting; SMTP notifications.
OUT OF SCOPE Odoo HR & Payroll base configuration (Requirements Specification v1.0.0); Kenyan statutory
payroll compliance (native Odoo); biometric device integration; native mobile app (browser
geo-API used).
ASSUMPTIONS Odoo 17 Enterprise on dedicated VPS (UK, 8 GB RAM / 4-core / 100 GB SSD). Odoo Documents
module is installed and active. All users access via HTTPS-enabled browser. StellarHR provides
the standard report template before UAT.
DEPENDENCIES documents module must be installed for folder auto-creation. documents.folder model must be
accessible via ORM from stellar_hr.
```

#### 1.4 Revision History

Version Date Author Summary of Changes
1.0.0 7 Apr 2026 P. Maina / E. Gathu Initial system design document.
1.1.0 Apr 2026 P. Maina / E. Gathu Added: document folder hierarchy (Sec 2.3, 5.2); session-based
check-in gate (Sec 2.4, 5.3); document type on upload (Sec 2.5,
5.2). Updated: data model, business logic, decisions
D-07/D-08/D-09.


### 2 FUNCTIONAL REQUIREMENTS

#### 2.1 Client & SLA Management

```
Req ID Requirement
FR-SLA-01 Client record must carry a client_type field (one-off | retainer).
FR-SLA-02 Each SLA record names the contracted HR functions and their recurrence schedule.
FR-SLA-03 Assigning an SLA to a client project must auto-create the corresponding HR function stubs.
FR-SLA-04 SLA templates must be reusable across clients with identical contractual obligations.
FR-SLA-05 Changing an SLA assignment must not retroactively modify live tasks; only future cycles are affected.
```
#### 2.2 HR Function & Task Orchestration

```
Req ID Requirement
FR-TASK-01 HR functions must be configurable with name, SLA link, and ordered sequence.
FR-TASK-02 Each task template defines: name, required attachments checklist, dependency list, and recurrence
rule.
FR-TASK-03 Task dependencies must be enforced at UI level — a blocked task shows its predecessor(s) and
prevents marking done.
FR-TASK-04 The system must auto-spawn tasks from templates at the configured recurrence interval (via ir.cron).
FR-TASK-05 Spawned tasks must inherit all configuration from their template, including dependency links.
FR-TASK-06 Task-level assignee feedback (comment text) must be mandatory before a task can be closed.
FR-TASK-07 All required attachment slots defined on the template must be fulfilled before task close.
FR-TASK-08 Task progress percentage must be linked to the specific user who recorded it.
FR-TASK-09 All task assignments and activity changes must trigger real-time notifications to the assignee.
```
#### 2.3 Document Folder Hierarchy H [REVISED v1.1]

#### Every project, task, and subtask must have a dedicated folder in the Odoo Documents module. Folders are

#### auto-created when their parent record is created and are arranged in a strict three-level hierarchy that mirrors

#### the record structure. Associates navigate to the folder directly from the record form via a smart button.

```
Req ID Requirement
FR-DOC-01 On project.project creation, auto-create a documents.folder named after the project under the root
workspace.
```

```
Req ID Requirement
FR-DOC-02 On project.task creation (parent_id IS NULL), auto-create a documents.folder named after the task,
nested inside the project folder.
FR-DOC-03 On project.task creation (parent_id IS NOT NULL / subtask), auto-create a documents.folder named
after the subtask, nested inside the parent task folder.
FR-DOC-04 Each record form (project, task, subtask) must display a "Documents" smart button showing the count of
files in its folder.
FR-DOC-05 Archiving or deleting a project/task must not delete its document folder — folders are retained for audit
purposes.
FR-DOC-06 Folder access rights must mirror the project access rights: only members of the project can access its
folder tree.
FR-DOC-07 Files uploaded directly to the task/subtask chatter must be automatically moved to the corresponding
folder.
Implementation note: Odoo 17 natively links one workspace folder per project (Documents > Settings >
Projects). The stellar_hr module extends this by programmatically calling documents.folder.create() on task and
subtask creation, using folder_id (parent) to build the hierarchy. The smart button uses an action_window
domain filtering on the linked folder_id.
```
#### 2.4 Session-Based Check-In Gate H [REVISED v1.1]

#### Task and subtask records must be read-only to associates unless an active check-in session exists for the

#### current user on the parent project. A session is a stellar.checkin.session record in the open state.

#### Checking out closes the session. This enforces that associates only work on tasks during their recorded shift —

#### every write action is traceable to a session.

```
Req ID Requirement
FR-SES-01 A stellar.checkin.session record is created when an associate clicks "Check In" on the project form.
FR-SES-02 A session captures: user_id, project_id, check_in_time, geo_lat, geo_lng, state (open | closed).
FR-SES-03 Only one open session per user per project is permitted at any time. Attempting a second check-in
raises a warning.
FR-SES-04 When no open session exists for the current user on a project, all task and subtask fields are rendered
as readonly in the OWL form view.
FR-SES-05 The read-only gate applies to: status changes, progress updates, feedback submission, file uploads,
and attachment fulfillment.
FR-SES-06 Read-only gate does NOT block: viewing task details, reading comments, downloading attached
documents.
FR-SES-07 Associates in stellar_hr.group_project_manager are exempt from the session gate — they can always
write.
```

```
Req ID Requirement
FR-SES-08 Checking out closes the session and re-applies the read-only state to all tasks in that project for that
user.
FR-SES-09 Session history (all check-in/out events) must be retained permanently for audit and shift accountability
reporting.
4
Implementation note: The read-only gate is implemented as an OWL component injected into the task form
view. On form load, it queries the server for an open session (stellar.checkin.session with state=open, user=uid,
project=project_id). If none found, the component sets all editable fields to attrs={"readonly": true} dynamically.
This is a UI-level gate; ORM-level write protection is also applied via a _check_session() method override on
project.task.write().
```
#### 2.5 Document Type on Upload H [REVISED v1.1]

#### Every file upload — whether to a project folder, task folder, subtask folder, or the task chatter — must be

#### classified with a Document Type before it is saved. Document types are configured system-wide by an

#### administrator. The type is stored on the ir.attachment record and is visible in folder views and reports.

```
Req ID Requirement
FR-DTYPE-01 A new model stellar.document.type holds the master list of document types (id, name, code, description,
active).
FR-DTYPE-02 On any file upload action in a task/subtask/project context, a Document Type field (Many2one →
stellar.document.type) must appear and be required before the upload is committed.
FR-DTYPE-03 ir.attachment is extended with + doc_type_id (Many2one → stellar.document.type, optional for
non-stellar contexts).
FR-DTYPE-04 The document type field must be visible in the folder view as a column and filterable.
FR-DTYPE-05 Administrators can add, rename, or archive document types from a dedicated configuration menu
without a developer.
FR-DTYPE-06 Document types must be included in report exports — each file listed in the report shows its type
alongside its name.
FR-DTYPE-07 If a required attachment slot (stellar.attachment.req) specifies an expected document type, the uploaded
file must match that type or a warning is raised.
Example document types (system-wide defaults): SLA Document · Employment Contract · NDA · Payslip ·
Compliance Report · ID / Passport · Photo Evidence · Policy Document · Offer Letter · Appraisal Form
```
#### 2.6 Onsite & Offsite Execution


Req ID Requirement
FR-GEO-01 Each project must carry an is_onsite flag set at project creation.
FR-GEO-02 For onsite projects, the check-in session (FR-SES-01) captures GPS coordinates at session open —
this constitutes the onsite check-in.
FR-GEO-03 For offsite tasks, GPS coordinates must additionally be captured at the moment the associate first writes
to a task (lazy geo-capture).
FR-GEO-04 Geo-location capture uses the browser navigator.geolocation API over HTTPS.
FR-GEO-05 Shift scheduling supports Day and Night shift types with configurable start and end times.
FR-GEO-06 The system must report on 8-hour shift cycle adherence per associate per day using session records.

#### 2.7 Role & Permission Model

Req ID Requirement
FR-ROLE-01 Only stellar_hr.group_project_manager users may assign tasks to associates.
FR-ROLE-02 HR Associates may update task progress and submit feedback, but cannot reassign tasks.
FR-ROLE-03 Task progress records are immutably linked to the user who created them.
FR-ROLE-04 PM and Admin roles are exempt from the session-based read-only gate (FR-SES-07).
FR-ROLE-05 Document type configuration is restricted to Admin role only.

#### 2.8 Reporting & Exports

Req ID Requirement
FR-REP-01 Hierarchical view: Client Project → HR Function → Tasks (with status, progress, pending items).
FR-REP-02 Incomplete tasks display a summary of pending items: missing attachments, incomplete predecessors,
open feedback.
FR-REP-03 Reports exported as QWeb PDF in StellarHR standard template; XLSX secondary.
FR-REP-04 Shift accountability report: each associate's session history against their scheduled 8-hour cycle.
FR-REP-05 Document audit report: per project/task, list all uploaded files with their document type and uploader.


### 3 NON-FUNCTIONAL REQUIREMENTS

Category Req ID Requirement
Performance NFR-P-01 Task list view (50 tasks) loads within 2 seconds on standard broadband from Kenya.
Performance NFR-P-02 Geo-location capture completes within 3 seconds of triggering check-in.
Performance NFR-P-03 Session state check (open/closed) on task form load completes within 300 ms — this is
called on every task open.
Performance NFR-P-04 Folder auto-creation on task/subtask create completes within the same ORM
transaction — no async lag.
Performance NFR-P-05 Scheduled task spawn (ir.cron) completes within 60 seconds for up to 500 template
instantiations.
Security NFR-S-01 All browser-server communication over TLS 1.2+.
Security NFR-S-02 GPS coordinates and session records are PII — access restricted by ir.rule to
assignee, PM, and Admin.
Security NFR-S-03 Document folders inherit project access rights — no cross-project file leakage.
Security NFR-S-04 The _check_session() ORM override must run on every project.task.write() call — it
cannot be bypassed by direct ORM scripts without Admin rights.
Security NFR-S-05 Document type configuration menu is restricted to Admin group via menuitem groups
attribute.
Scalability NFR-SC-01 Supports up to 100 concurrent users and 10,000 active tasks without degradation.
Scalability NFR-SC-02 PostgreSQL indexes on: task_id, user_id, project_id, session state, doc_type_id,
folder_id.
Maintainability NFR-M-01 All custom models prefixed stellar.* — no exceptions.
Maintainability NFR-M-02 Business logic in model methods only; not in controllers or views.
Maintainability NFR-M-03 Data migration script for every schema change post-v1.
Maintainability NFR-M-04 Document type list must be manageable by a non-developer Admin — no XML edits
required.


### 4 HIGH-LEVEL DESIGN

#### 4.1 System Architecture

#### The stellar_hr module sits as a single application layer on top of Odoo 17 core. No separate microservices or

#### external databases are introduced. All state lives in the single PostgreSQL instance. Three new cross-cutting

#### concerns introduced in v1.1 — folder management, session gating, and document typing — are handled entirely

#### within the module via ORM hooks and OWL component injections.

```
Client layer Web browser (Odoo OWL frontend) · Mobile browser for geo-capture and check-in
Custom module stellar_hr — SLA engine, task orchestrator, folder service, session gate, geo service,
doc-type service, role guards, report builder
Odoo Documents documents.folder — auto-created hierarchy; documents.document — typed file storage
Odoo Core project.project · project.task · res.partner · hr.employee · ir.attachment · mail.thread · ir.rule ·
ir.cron
Infrastructure PostgreSQL 15 · Nginx · Ubuntu 24 LTS · 8 GB RAM / 4-core / 100 GB SSD · UK VPS
External SMTP gateway (notifications) · Browser geolocation API (navigator.geolocation)
```
#### 4.2 Module Boundaries

```
Sub-component Key Models Responsibility
SLA Engine stellar.sla,
stellar.hr.function
Client type, SLA definitions, HR function mappings.
Triggers task template spawning.
Task Orchestrator stellar.task.template,
project.task (ext)
Template definitions, dependency enforcement,
recurrence scheduling, task spawn lifecycle.
Folder Service H documents.folder (ext),
project hooks
Auto-creates 3-level folder hierarchy on
project/task/subtask creation. Provides smart-button
document count.
Session Gate H stellar.checkin.session,
project.task (ext)
Manages check-in/out sessions per user per project.
Enforces read-only gate on task writes when no open
session exists.
Doc-Type Service H stellar.document.type,
ir.attachment (ext)
System-wide document type registry. Injects type
selector into upload widgets. Validates type on
attachment.req fulfilment.
Geo & Attendance stellar.work.schedule Onsite/offsite distinction. Shift scheduling. 8-hour cycle
accountability. Geo coords now captured on session
open.
```

```
Sub-component Key Models Responsibility
Task Extensions stellar.task.feedback,
stellar.attachment.req,
stellar.task.progress
```
```
Per-task feedback, required attachment gating,
assignee-linked progress tracking.
```
```
Report Builder stellar.report.config, QWeb,
XLSX
```
Hierarchical PDF/XLSX exports. Document audit
report. Shift accountability report.
Rows highlighted in amber are new or revised sub-components introduced in v1.1.

#### 4.3 Integration Points

```
Integration Direction Mechanism Purpose
SMTP Gateway Outbound Odoo mail.mail → SMTP Payslip, leave approvals, task assignment
notifications
Browser Geolocation Inbound
(client)
```
```
navigator.geolocation.getCurrentPo
sition()
```
```
GPS capture on session check-in; lazy
offsite task capture
documents.folder Internal
ORM
```
```
documents.folder.create() on
post-create hook
```
```
Auto-create project/task/subtask folder
hierarchy
ir.cron Internal Scheduled action on
stellar.task.template
```
```
Recurring task spawn for retainer SLA
cycles
QWeb PDF Engine Internal report.action → QWeb template StellarHR-branded PDF report generation
PostgreSQL Internal ORM + direct query All persistent state; indexed on task_id,
user_id, project_id, session state, folder_id,
doc_type_id
```

### 5 LOW-LEVEL DESIGN

#### 5.1 Data Model Overview

#### All custom models are prefixed stellar.*. Native Odoo models are extended using Python _inherit —

#### additive changes only. Three new models and two extended native models are introduced in v1.1.

Extended Native Models

#### res.partner — + client_type (Selection: one_off | retainer), + sla_ids (M2M → stellar.sla)

#### project.project — + is_onsite (Boolean), + client_id (M2O → res.partner), + hr_function_ids (O2M), + folder_id (M2O

```
→ documents.folder) H
```
#### project.task — + geo_lat (Float), + geo_lng (Float), + assignee_progress (Integer), + required_attachment_ids (O2M), +

```
feedback_ids (O2M), + folder_id (M2O → documents.folder) H
```
#### ir.attachment — + doc_type_id (M2O → stellar.document.type) H

Core Custom Models

#### stellar.sla — id, name, client_type, hr_function_ids (O2M)

#### stellar.hr.function — id, name, sla_id (M2O), task_template_ids (O2M), sequence

#### stellar.task.template — id, name, hr_function_id (M2O), depends_on_ids (M2M self), required_attachment_def

```
(JSON Text), recurrence_rule, active
```
#### stellar.document.type H — id, name, code (Char, unique), description (Text), active (Boolean)

Session & Geo Models H

#### stellar.checkin.session H — id, user_id (M2O → res.users), project_id (M2O → project.project), check_in_time

```
(Datetime), check_out_time (Datetime), state (open | closed), geo_lat (Float), geo_lng (Float) — replaces previous
stellar.task.checkin
```
#### stellar.work.schedule — id, user_id (M2O → res.users), shift_type (day | night), start_time (Float), end_time (Float),

```
cycle_hours (default 8)
```
Task Extension Models

#### stellar.task.feedback — id, task_id (M2O), author_id (M2O → res.users), comment (Text), create_date

#### stellar.attachment.req — id, task_id (M2O), label (Char), attachment_id (M2O → ir.attachment),

```
expected_doc_type_id (M2O → stellar.document.type) H, is_fulfilled (Boolean)
```
#### stellar.task.progress — id, task_id (M2O), user_id (M2O → res.users), progress_pct (Integer), notes (Text),

write_date
Reporting

#### stellar.report.config — id, template_file (Binary), grouping (selection), output_format (pdf | xlsx)

#### 5.2 Custom Models Reference H

#### stellar.checkin.session [NEW v1.1 — replaces stellar.task.checkin]


```
Field Type Constraint / Default Description
user_id Many2one res.users, Required Associate who checked in
project_id Many2one project.project, Required Project this session covers
check_in_time Datetime Required, default now() Session open timestamp
check_out_time Datetime Optional Session close timestamp; null = still open
state Selection open | closed; default
open
```
```
Session state — drives read-only gate
```
geo_lat Float Optional Latitude at check-in
geo_lng Float Optional Longitude at check-in
SQL constraint: UNIQUE(user_id, project_id) WHERE state = 'open' — enforced via PostgreSQL partial unique index to allow
multiple closed sessions per user/project.

#### stellar.document.type [NEW v1.1]

```
Field Type Constraint / Default Description
name Char Required Display name, e.g. "SLA Document"
code Char Required, unique Short code, e.g. "SLA", "CONTRACT", "PAYSLIP"
description Text Optional Guidance text shown to users on upload
active Boolean Default True Archive flag — archived types hidden from upload
selector
```
#### stellar.attachment.req [UPDATED v1.1 — added expected_doc_type_id]

```
Field Type Constraint / Default Description
task_id Many2one project.task, Required Parent task
label Char Required Human-readable slot name, e.g. "Signed SLA"
attachment_id Many2one ir.attachment, Optional Fulfilled when set
expected_doc_type_id Many2one stellar.document.type,
Optional
```
```
If set, the uploaded file must match this type
```
```
is_fulfilled Boolean Computed True when attachment_id is set and doc_type
matches
```
#### 5.3 Business Logic H

#### Folder auto-creation [NEW v1.1]

#### Three @api.model_create_multi post-create hooks:

#### (1) project.project.create() → calls _stellar_create_project_folder() which calls documents.folder.create({name:


#### project.name, parent_folder_id: root_workspace_id}) and writes folder_id back to the project.

#### (2) project.task.create() where parent_id IS NULL → creates folder under project.folder_id.

#### (3) project.task.create() where parent_id IS NOT NULL → creates folder under parent_task.folder_id.

#### The root_workspace_id is read from ir.config_parameter key "stellar_hr.documents_root_folder_id", set by the

#### module installer.

#### Session gate — read-only enforcement [NEW v1.1]

#### project.task.write() is overridden with a _check_session() pre-check. The method queries: SELECT id FROM

#### stellar_checkin_session WHERE user_id=%s AND project_id=%s AND state='open'. If no row is returned AND

#### the current user is not in stellar_hr.group_project_manager, an AccessError is raised: "Check in to [Project

#### Name] before updating tasks."

#### The OWL StellarSessionGate component additionally performs a client-side RPC check on form load and sets

#### field readonly attrs dynamically — providing immediate UI feedback without waiting for a save attempt.

#### Document type injection [NEW v1.1]

#### The OWL StellarUploadWidget extends Odoo's native many2many_binary widget. When a file is selected for

#### upload, the widget injects a Many2one field (stellar.document.type) into the upload dialog. The upload is blocked

#### (Promise rejected) if doc_type_id is null. On save, doc_type_id is written to ir.attachment via a JSON-RPC

#### call_kw to ir.attachment.write(). For stellar.attachment.req fulfilment, a @api.constrains check verifies

#### attachment.doc_type_id == req.expected_doc_type_id when expected is set.

#### Task spawn (ir.cron)

#### The cron job stellar_hr.action_spawn_tasks queries stellar.task.template records where recurrence_rule !=

#### "none" and last_spawn_date is past due. _spawn_task() creates project.task, copies dependency links,

#### instantiates attachment req slots, and triggers the folder auto-creation hook.

#### Dependency enforcement

#### project.task._action_done() override checks all tasks in depends_on_task_ids have stage_id.is_closed == True

#### before proceeding. If blocked, UserError is raised listing blocking task names. UI-level block, not a DB

#### constraint.

#### 5.4 Security Rules

```
Rule ID Model Applied To Domain / Filter Purpose
stellar_hr.rule_session_own stellar.checkin.session Associate ("user_id","=",uid) Associates see only
their own sessions
stellar_hr.rule_task_progres
s_own
```
```
stellar.task.progress Associate ("user_id","=",uid) Associates write
progress on their own
tasks only
stellar_hr.rule_folder_projec
t
```
```
documents.folder Associate project membership
filter
```
```
Folder access mirrors
project membership
```

```
Rule ID Model Applied To Domain / Filter Purpose
stellar_hr.rule_client_pm res.partner (client_type
set)
```
```
PM + Admin groups filter Client & SLA data
hidden from Associate
role
stellar_hr.rule_doctype_ad
min
```
```
stellar.document.type Admin only groups filter Only Admin can
create/edit/archive
document types
stellar_hr.rule_report_config stellar.report.config Admin only groups filter Report template config
restricted to Admin
```
#### 5.5 API Surface

#### The module adds two controller routes beyond standard Odoo JSON-RPC, both protected by session

#### authentication:

```
POST /stellar_hr/checkin — body: {project_id, lat, lng} — creates
stellar.checkin.session (state=open) — returns {session_id, state, check_in_time}
POST /stellar_hr/checkout — body: {session_id} — sets stellar.checkin.session.state =
closed, check_out_time = now() — returns {session_id, state, check_out_time,
duration_hours}
Both routes require a valid Odoo session cookie and enforce user ownership (the session's user_id must equal
the authenticated user — enforced at ORM level via ir.rule, not only at controller level).
```

### 6 DECISIONS & TRADE-OFFS

Decisions D-01 through D-06 are carried forward from v1.0 unchanged. D-07, D-08, and D-09 are new decisions introduced
in v1.1.

```
D-01 Geo-location via browser API (not native mobile app) ACCEPTE
D
Chosen approach Browser-native navigator.geolocation over HTTPS
Alternative considered Native iOS/Android app with background location
Rationale No separate app to build or maintain. HTTPS already required for Odoo. Geo accuracy
sufficient for compliance logging. Background tracking not required since capture is
user-triggered at session check-in.
D-02 Task dependency enforcement at UI level, not DB constraint ACCEPTED
Chosen approach UserError raised in project.task._action_done() override
Alternative considered SQL CHECK constraint or ir.rule blocking write
Rationale UI-level block surfaces a clear, actionable error listing blocking tasks by name. A DB
constraint produces a cryptic psycopg2 IntegrityError. Admins retain ability to override in edge
cases.
D-03 Recurrence rule stored on stellar.task.template (per template) ACCEPTE
D
Chosen approach recurrence_rule field on stellar.task.template
Alternative considered Single recurrence rule on stellar.sla (per contract)
Rationale Different HR functions within the same SLA may have different recurrence frequencies.
Template-level storage supports this without changing the SLA record.
D-04 QWeb PDF as primary report format, XLSX secondary ACCEPTED —
pending
template
receipt
Chosen approach report.action with QWeb + openpyxl XLSX writer
Alternative considered XLSX only
Rationale QWeb PDF provides a branded, tamper-evident delivery artefact. XLSX retained for
client-side manipulation. QWeb template to be finalised once StellarHR standard template is
received.
```

D-05 Custom security group stellar_hr.group_project_manager ACCEPTE
D
Chosen approach New res.groups separate from Odoo's native Project Manager role
Alternative considered Reuse Odoo built-in project.group_project_manager
Rationale Reusing the native group couples logic to Odoo's PM role which has broader permissions. A
separate group gives precise control and survives Odoo upgrades.

D-06 Single Odoo instance, no microservices ACCEPTED

Chosen approach All logic in stellar_hr module on shared Odoo/PostgreSQL stack
Alternative considered Separate FastAPI microservice for geo/reporting
Rationale A microservice adds deployment complexity and a second database — unjustified at current
scale (~100 users). Revisit if users exceed 200.

D-07 [REV] Three-level folder hierarchy auto-created via ORM post-create
hooks

ACCEPTE
D
Chosen approach documents.folder.create() called in @api.model_create_multi post hooks on project and task
Alternative considered Manual folder creation by users; or flat single project workspace
Rationale Manual creation is error-prone and inconsistent. A flat workspace becomes unnavigable at
scale (100+ tasks per project). Programmatic creation ensures every record has a folder from
day one without user effort. Hooks are lightweight and complete within the same DB
transaction — no async risk.

D-08 [REV] Session-based gate implemented at both UI (OWL) and ORM (write
override) levels

```
ACCEPTE
D
```
Chosen approach OWL component sets readonly attrs on form load; _check_session() in project.task.write()
Alternative considered ORM-only (no UI feedback until save); or UI-only (bypassable via direct ORM/API calls)
Rationale ORM-only gives poor UX — the associate fills in a form only to get an error on save. UI-only
is insecure — direct API calls bypass the gate. Dual enforcement gives immediate user
feedback AND backend integrity. The OWL component is the UX layer; the ORM override is
the security layer.


D-09 [REV] System-wide document type list (not per-project) ACCEPTE
D
Chosen approach Single stellar.document.type model; one global list for all projects
Alternative considered Per-project document type configuration
Rationale Per-project types add significant configuration overhead — StellarHR would need to configure
types for every new client project. A system-wide list is configured once by Admin and applies
everywhere, reducing maintenance. If per-project filtering is needed in future, it can be added
as an optional M2M override on project.project without changing the core model.


### 7 IMPLEMENTATION ROADMAP

Phase Timeline Deliverables
Phase 1 — Foundation Weeks 1–2 Module scaffold; stellar.sla, stellar.hr.function, stellar.task.template;
res.partner & project.project extensions; basic task spawn cron; unit tests.
Phase 2 — Folder Hierarchy
H

Week 3 documents.folder auto-creation hooks on project/task/subtask; smart button
document counts; folder access rights mirroring project membership;
chatter attachment routing.
Phase 3 — Session Gate H Week 4 stellar.checkin.session model; check-in/out controller routes; OWL
StellarSessionGate component; project.task.write() _check_session()
override; PM exemption; session history view.
Phase 4 — Document Types
H

Week 5 stellar.document.type model + Admin config menu; OWL
StellarUploadWidget; ir.attachment extension; stellar.attachment.req
doc_type validation; document audit report.
Phase 5 — Task Execution Week 6 Dependency enforcement; feedback/progress models; attachment gating;
geo lazy-capture for offsite; shift scheduling models.
Phase 6 — Reporting Week 7 stellar.report.config; QWeb PDF template (awaiting StellarHR standard
template); XLSX secondary; hierarchical dashboard; shift accountability
report.
Phase 7 — UAT & Hardening Weeks 8–9 UAT with StellarHR stakeholders; bug fixes; performance profiling; index
optimisation; security audit; go-live checklist.
Note: Phases 2, 3, and 4 (marked H) are new phases introduced by the v1.1 revisions. Total timeline extends by
~2 weeks versus v1.0. QWeb report template finalisation remains blocked on receipt of StellarHR's standard
template.


### 8 GLOSSARY

```
Term Definition
Check-in Session A stellar.checkin.session record in the open state. One session per user per project.
Required before any task write.
Document Type A stellar.document.type record classifying an uploaded file (e.g., SLA, Contract, Payslip).
System-wide, admin-managed.
Folder Hierarchy The three-level documents.folder structure: Project folder → Task folder → Subtask folder.
Auto-created by stellar_hr hooks.
HR Associate A StellarHR staff member assigned to execute HR service tasks for clients.
HR Function A named group of related tasks contractually bound to an SLA (e.g., Payroll Processing).
ir.cron Odoo's native scheduled action mechanism. Used to trigger recurring task spawning.
ir.rule Odoo's record-level access rule system. Used to restrict visibility of sensitive records.
OWL Odoo Web Library — the JavaScript frontend framework used in Odoo 17.
Project Manager (PM) A StellarHR user with stellar_hr.group_project_manager — exempt from session gate; the
only role that can assign tasks.
QWeb Odoo's XML-based templating engine, used for PDF report generation.
Read-only Gate The UI + ORM mechanism that prevents task writes when no open session exists for the
current user.
Retainer Client A client on a recurring engagement, triggering periodic task spawning from SLA templates.
Session Gate See Read-only Gate.
SLA Service Level Agreement — defines the HR functions and delivery frequency contracted to
a client.
Spawn Automated creation of project.task records from stellar.task.template definitions by ir.cron.
stellar_hr The custom Odoo module delivered under this design document.
VPS Virtual Private Server — dedicated hosting environment for the Odoo installation (UK, 8 GB
RAM / 4-core / 100 GB SSD).
```
### Document Sign-Off

```
Prepared by Patrick N. Maina / Emmanuel Gathu — MobiPine Limited
Document Version 1.1.
```

Date April 2026
Status Draft v1.1 — incorporates rev1 scope changes; pending client review


