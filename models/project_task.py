from odoo import api, fields, models
from odoo.exceptions import AccessError, UserError, ValidationError


class ProjectTask(models.Model):
    _inherit = "project.task"

    _SESSION_GUARDED_FIELDS = {
        "name",
        "description",
        "project_id",
        "parent_id",
        "stage_id",
        "user_ids",
        "partner_id",
        "date_deadline",
        "priority",
        "tag_ids",
        "planned_hours",
        "allocated_hours",
    }

    documents_folder_id = fields.Many2one(
        "documents.document",
        string="Documents Folder",
        copy=False,
        index="btree_not_null",
        domain="[('type', '=', 'folder'), ('shortcut_document_id', '=', False)]",
        readonly=True,
        help="Task-specific folder in Documents. Subtasks are nested under their parent task folder.",
    )
    document_count = fields.Integer(
        string="Documents",
        compute="_compute_documents",
    )
    task_template_id = fields.Many2one(
        "mobipine_project.task_template",
        string="Spawn Template",
        readonly=True,
        index=True,
        copy=False,
    )
    hr_function_id = fields.Many2one(
        "mobipine_project.hr_function",
        string="HR Function",
        readonly=True,
        index=True,
        copy=False,
    )
    cycle_date = fields.Date(string="Spawn Cycle Date", readonly=True, index=True, copy=False)
    spawned_by_cron = fields.Boolean(string="Spawned by Cron", readonly=True, copy=False)
    current_user_open_session_id = fields.Many2one(
        "mobipine_project.checkin_session",
        compute="_compute_current_user_session",
        string="My Open Session",
    )
    current_user_has_open_session = fields.Boolean(
        compute="_compute_current_user_session",
        string="Has Open Session",
    )
    
    # Phase 2: Task Dependencies
    parent_task_ids = fields.Many2many(
        "project.task",
        "project_task_dependency_rel",
        "task_id",
        "parent_id",
        string="Task Dependencies",
        help="Parent/predecessor tasks that must be completed before this task.",
    )
    child_task_ids = fields.Many2many(
        "project.task",
        "project_task_dependency_rel",
        "parent_id",
        "task_id",
        string="Dependent Tasks",
        help="Subtasks that depend on this task.",
    )
    blocked_by_tasks = fields.Many2many(
        "project.task",
        compute="_compute_blocked_by_tasks",
        string="Blocked By",
        help="Currently incomplete dependencies preventing this task from being marked done.",
    )
    can_move_to_done = fields.Boolean(
        compute="_compute_can_move_to_done",
        string="Can Close",
        help="True if all dependencies are met and required attachments fulfilled.",
    )
    geo_lat = fields.Float(digits=(16, 8), string="Latitude")
    geo_lng = fields.Float(digits=(16, 8), string="Longitude")
    
    # Phase 2: Feedback & Progress
    feedback_ids = fields.One2many(
        "stellar.task.feedback",
        "task_id",
        string="Feedback",
        help="Immutable feedback records per assignee.",
    )
    feedback_count = fields.Integer(compute="_compute_feedback_count")
    progress_ids = fields.One2many(
        "stellar.task.progress",
        "task_id",
        string="Progress Records",
        help="User-linked progress updates.",
    )
    assignee_progress_pct = fields.Integer(
        compute="_compute_assignee_progress",
        string="Progress %",
    )
    
    # Phase 2: Attachment Requirements
    attachment_req_ids = fields.One2many(
        "stellar.attachment.req",
        "task_id",
        string="Required Attachments",
        help="Checklist of required file uploads.",
    )
    attachment_req_count = fields.Integer(compute="_compute_attachment_req_count")
    attachment_req_fulfilled = fields.Integer(compute="_compute_attachment_req_fulfilled")

    _sql_constraints = [
        (
            "mobipine_project_task_template_cycle_uniq",
            "unique(project_id, task_template_id, cycle_date)",
            "A spawned task already exists for this template and cycle in the selected project.",
        )
    ]

    @api.depends("documents_folder_id")
    def _compute_documents(self):
        document_model = self.env["documents.document"].sudo()
        for task in self:
            if not task.documents_folder_id:
                task.document_count = 0
                continue
            task.document_count = document_model.search_count(
                [
                    ("type", "in", ("binary", "url")),
                    ("id", "child_of", task.documents_folder_id.id),
                ]
            )

    @api.depends("project_id", "project_id.checkin_session_ids.state", "project_id.checkin_session_ids.user_id")
    def _compute_current_user_session(self):
        session_model = self.env["mobipine_project.checkin_session"]
        uid = self.env.user.id
        for task in self:
            open_session = session_model.search(
                [
                    ("project_id", "=", task.project_id.id),
                    ("user_id", "=", uid),
                    ("state", "=", "open"),
                ],
                limit=1,
                order="check_in_time desc",
            ) if task.project_id else session_model.browse()
            task.current_user_open_session_id = open_session
            task.current_user_has_open_session = bool(open_session)

    @api.depends("parent_task_ids", "parent_task_ids.stage_id")
    def _compute_blocked_by_tasks(self):
        """Find incomplete dependencies."""
        done_stage = self.env["project.stage"].search(
            [("name", "=ilike", "Done")], limit=1
        )
        for task in self:
            blocked = task.parent_task_ids.filtered(
                lambda t: (not done_stage) or (t.stage_id != done_stage)
            )
            task.blocked_by_tasks = blocked

    @api.depends("blocked_by_tasks", "attachment_req_ids.is_fulfilled", "feedback_ids")
    def _compute_can_move_to_done(self):
        """Check if task can be marked done."""
        for task in self:
            # All dependencies must be complete
            deps_met = len(task.blocked_by_tasks) == 0
            # All required attachments must be fulfilled
            attachments_ok = not task.attachment_req_ids or all(
                req.is_fulfilled for req in task.attachment_req_ids
            )
            # At least one feedback record from an assignee
            feedback_ok = len(task.feedback_ids) > 0
            task.can_move_to_done = deps_met and attachments_ok and feedback_ok

    @api.depends("feedback_ids")
    def _compute_feedback_count(self):
        for task in self:
            task.feedback_count = len(task.feedback_ids)

    @api.depends("progress_ids")
    def _compute_assignee_progress(self):
        """Get latest progress percent."""
        for task in self:
            latest = task.progress_ids.sorted(key=lambda p: p.create_date, reverse=True)
            task.assignee_progress_pct = latest[0].progress_pct if latest else 0

    @api.depends("attachment_req_ids")
    def _compute_attachment_req_count(self):
        for task in self:
            task.attachment_req_count = len(task.attachment_req_ids)

    @api.depends("attachment_req_ids.is_fulfilled")
    def _compute_attachment_req_fulfilled(self):
        for task in self:
            task.attachment_req_fulfilled = sum(
                1 for req in task.attachment_req_ids if req.is_fulfilled
            )

    @api.model_create_multi
    def create(self, vals_list):
        """Create tasks with session guard check."""
        self._check_session_guard_for_create(vals_list)
        tasks = super().create(vals_list)
        tasks._create_missing_documents_folders()
        return tasks

    def write(self, vals):
        """Session gate enforcement and soft-delete folder protection."""
        self._check_session_guard()
        result = super().write(vals)
        # Auto-create missing folders if task had no folder
        self._create_missing_documents_folders()
        return result

    def unlink(self):
        """Soft-delete folder: unlink task but keep folder (FR-DOC-05)."""
        # Save folder IDs before deletion
        folder_ids = [task.documents_folder_id.id for task in self if task.documents_folder_id]
        result = super().unlink()
        # Folders are preserved — do not cascade delete
        return result

    def _check_session_guard_for_create(self, vals_list):
        """Check session before allowing task creation (non-PM users)."""
        if self.env.user.has_group("mobipine_odoo_project_management.group_project_manager"):
            return  # PMs are exempt
        for vals in vals_list:
            if "project_id" in vals:
                project = self.env["project.project"].browse(vals["project_id"])
                session = self.env["mobipine_project.checkin_session"].search(
                    [
                        ("project_id", "=", project.id),
                        ("user_id", "=", self.env.user.id),
                        ("state", "=", "open"),
                    ]
                )
                if not session:
                    raise AccessError(
                        f"You must check in to '{project.name}' before creating tasks."
                    )

    def _check_session_guard(self):
        """Enforce session-based read-only gate (FR-SES-04)."""
        if self.env.user.has_group("mobipine_odoo_project_management.group_project_manager"):
            return  # PMs are exempt
        
        for task in self:
            session = self.env["mobipine_project.checkin_session"].search(
                [
                    ("project_id", "=", task.project_id.id),
                    ("user_id", "=", self.env.user.id),
                    ("state", "=", "open"),
                ]
            )
            if not session:
                raise AccessError(
                    f"No open session for project '{task.project_id.name}'. "
                    "Please check in before updating tasks."
                )

    def _get_parent_documents_folder(self):
        """Find parent folder in hierarchy."""
        self.ensure_one()
        if self.parent_id and self.parent_id.documents_folder_id:
            return self.parent_id.documents_folder_id
        if self.project_id and self.project_id.documents_folder_id:
            return self.project_id.documents_folder_id
        return self.env["documents.document"]

    def _prepare_folder_values(self):
        """Prepare folder creation values."""
        self.ensure_one()
        parent_folder = self._get_parent_documents_folder()
        vals = {
            "name": self.name,
            "type": "folder",
            "company_id": self.company_id.id or False,
        }
        if parent_folder:
            vals["folder_id"] = parent_folder.id
        return vals

    def _create_missing_documents_folders(self):
        """Auto-create document folder for task/subtask if not exists (FR-DOC-02, FR-DOC-03)."""
        documents_folder = self.env["documents.document"]
        for task in self.filtered(lambda t: not t.documents_folder_id):
            try:
                folder_vals = task._prepare_folder_values()
                if folder_vals:
                    folder = documents_folder.create(folder_vals)
                    task.write({"documents_folder_id": folder.id})
            except Exception as e:
                # Graceful fallback if Documents module not ready
                self.env.cr.rollback()
                pass

    def action_check_in(self):
        for task in self:
            if task.project_id:
                task.project_id.action_check_in()
        return True

    def action_check_out(self):
        for task in self:
            if task.project_id:
                task.project_id.action_check_out()
        return True

    def action_view_task_documents(self):
        self.ensure_one()
        if not self.documents_folder_id:
            raise UserError("No documents folder is linked to this task yet.")
        action = self.env["ir.actions.actions"]._for_xml_id("documents.document_action")
        action["domain"] = [("id", "child_of", self.documents_folder_id.id)]
        action["context"] = {
            "default_folder_id": self.documents_folder_id.id,
            "searchpanel_default_folder_id": self.documents_folder_id.id,
        }
        return action
