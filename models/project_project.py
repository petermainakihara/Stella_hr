from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class ProjectProject(models.Model):
    _inherit = "project.project"

    def _stellar_get_user_employee(self):
        employee = self.env["hr.employee"].sudo().search(
            [("user_id", "=", self.env.user.id)],
            limit=1,
            order="id desc",
        )
        if employee:
            return employee
        user = self.env.user
        employee = getattr(user, "employee", False)
        if getattr(employee, "_name", None) == "hr.employee" and employee:
            return employee
        employee = getattr(user, "employee_id", False)
        if getattr(employee, "_name", None) == "hr.employee" and employee:
            return employee
        employees = getattr(user, "employee_ids", False)
        return employees[:1] if getattr(employees, "_name", None) == "hr.employee" and employees else False

    is_onsite = fields.Boolean(string="Onsite Project", default=False)
    client_partner_id = fields.Many2one(
        "res.partner",
        string="StellarHR Client",
        domain=[("client_type", "!=", False)],
        groups="mobipine_odoo_project_management.group_project_manager,base.group_system",
    )
    sla_ids = fields.Many2many(
        "mobipine_project.sla",
        "project_sla_rel",
        "project_id",
        "sla_id",
        string="Assigned SLAs",
        groups="mobipine_odoo_project_management.group_project_manager,base.group_system",
    )
    sla_id = fields.Many2one(
        "mobipine_project.sla",
        string="Primary SLA",
        groups="mobipine_odoo_project_management.group_project_manager,base.group_system",
    )
    shift_type = fields.Selection(
        selection=[("day", "Day"), ("night", "Night")],
        string="Shift Type",
        default="day",
    )
    shift_start = fields.Float(string="Shift Start Hour", default=8.0)
    shift_end = fields.Float(string="Shift End Hour", default=16.0)
    checkin_session_ids = fields.One2many(
        "mobipine_project.checkin_session",
        "project_id",
        string="Check-in Sessions",
    )
    current_user_open_session_id = fields.Many2one(
        "mobipine_project.checkin_session",
        compute="_compute_current_user_session",
        string="My Open Session",
    )
    current_user_has_open_session = fields.Boolean(
        compute="_compute_current_user_session",
        string="Has Open Session",
    )
    checkin_session_count = fields.Integer(
        compute="_compute_checkin_session_count",
        string="Session Count",
    )
    sla_function_ids = fields.Many2many(
        "mobipine_project.hr_function",
        compute="_compute_sla_function_ids",
        string="HR Functions",
    )

    @api.onchange("client_partner_id")
    def _onchange_client_partner_id(self):
        for record in self:
            if record.client_partner_id:
                record.partner_id = record.client_partner_id

    @api.constrains("shift_type", "shift_start", "shift_end")
    def _check_shift_window(self):
        for record in self:
            if record.shift_start < 0 or record.shift_start > 24:
                raise ValidationError("Shift start hour must be between 0 and 24.")
            if record.shift_end < 0 or record.shift_end > 24:
                raise ValidationError("Shift end hour must be between 0 and 24.")
            if record.shift_type == "day" and record.shift_end <= record.shift_start:
                raise ValidationError("For a day shift, end hour must be greater than start hour.")
            if record.shift_type == "night" and record.shift_end == record.shift_start:
                raise ValidationError("For a night shift, start and end hours cannot be equal.")

    @api.depends("checkin_session_ids.state", "checkin_session_ids.user_id")
    def _compute_current_user_session(self):
        user_id = self.env.user.id
        session_model = self.env["mobipine_project.checkin_session"]
        for project in self:
            open_session = session_model.search(
                [
                    ("user_id", "=", user_id),
                    ("state", "=", "open"),
                ],
                limit=1,
                order="check_in_time desc",
            )
            project.current_user_open_session_id = open_session
            project.current_user_has_open_session = bool(open_session)

    @api.depends("checkin_session_ids")
    def _compute_checkin_session_count(self):
        for project in self:
            project.checkin_session_count = len(project.checkin_session_ids)

    @api.depends("sla_id", "sla_id.hr_function_ids")
    def _compute_sla_function_ids(self):
        for project in self:
            project.sla_function_ids = project.sla_id.hr_function_ids if project.sla_id else False

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._auto_create_hr_stubs_from_slas()
        return records

    def write(self, vals):
        if "sla_id" in vals or "sla_ids" in vals:
            self._block_sla_edit_if_spawned_tasks()
        result = super().write(vals)
        if "sla_id" in vals or "sla_ids" in vals:
            self._auto_create_hr_stubs_from_slas()
        return result

    def _block_sla_edit_if_spawned_tasks(self):
        task_model = self.env["project.task"]
        for record in self:
            if task_model.search_count([
                ("project_id", "=", record.id),
                ("spawned_by_cron", "=", True),
            ]):
                raise ValidationError(
                    "Cannot change SLA assignment because recurring live tasks already exist. "
                    "Only future cycles should be changed in templates."
                )

    def _auto_create_hr_stubs_from_slas(self):
        """Auto-create HR function task stubs when SLA is assigned (FR-SLA-03)."""
        task_model = self.env["project.task"]
        template_model = self.env["mobipine_project.task_template"]
        for record in self:
            slas = record.sla_ids if record.sla_ids else ([record.sla_id] if record.sla_id else [])
            for sla in slas:
                templates = template_model.search([
                    ("sla_id", "=", sla.id),
                    ("active", "=", True),
                ])
                for template in templates:
                    existing = task_model.search_count([
                        ("project_id", "=", record.id),
                        ("task_template_id", "=", template.id),
                        ("spawned_by_cron", "=", False),
                    ], limit=1)
                    if existing:
                        continue
                    vals = {
                        "name": "%s - %s" % (template.hr_function_id.name, template.name),
                        "project_id": record.id,
                        "description": template.description or False,
                        "task_template_id": template.id,
                        "hr_function_id": template.hr_function_id.id,
                        "spawned_by_cron": False,
                    }
                    if record.user_id:
                        vals["user_ids"] = [(4, record.user_id.id)]
                    task_model.create(vals)

    def action_check_in(self):
        self.ensure_one()
        employee = self._stellar_get_user_employee()
        if not employee:
            raise UserError("You need an employee record to check in.")
        return employee._stellar_get_attendance_checkin_action(
            project_id=self.id,
            partner_id=self.client_partner_id.id or self.partner_id.id,
        )

    def action_check_out(self):
        self.ensure_one()
        employee = self._stellar_get_user_employee()
        if not employee:
            raise UserError("You need an employee record to check out.")
        employee._stellar_register_attendance_checkout()
        return True

    def action_view_checkin_sessions(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "mobipine_odoo_project_management.action_project_checkin_session"
        )
        action["domain"] = [("project_id", "=", self.id)]
        action["context"] = {
            "default_project_id": self.id,
            "search_default_project_id": self.id,
        }
        return action
