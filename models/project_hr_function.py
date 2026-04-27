from odoo import api, fields, models


class ProjectHRFunction(models.Model):
    _name = "mobipine_project.hr_function"
    _description = "SLA HR Function"
    _order = "sequence, id"

    name = fields.Char(required=True)
    code = fields.Char(default="New", copy=False, readonly=True, index=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    sla_id = fields.Many2one("mobipine_project.sla", required=True, ondelete="cascade", index=True)
    project_id = fields.Many2one("project.project", string="Project", ondelete="cascade", index=True)
    task_template_ids = fields.One2many(
        "mobipine_project.task_template",
        "hr_function_id",
        string="Task Templates",
    )
    task_count = fields.Integer(compute="_compute_task_count", string="Tasks")
    project_task_count = fields.Integer(
        compute="_compute_project_task_count",
        string="Tasks (Project)",
        help="Number of tasks for this HR function in the currently viewed project.",
    )

    _sql_constraints = [
        (
            "mobipine_project_hr_function_name_sla_uniq",
            "unique(name, sla_id)",
            "HR Function name must be unique per SLA.",
        ),
        ("mobipine_project_hr_function_code_uniq", "unique(code)", "HR Function code must be unique."),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        sequence = self.env["ir.sequence"]
        for vals in vals_list:
            if vals.get("code", "New") == "New":
                vals["code"] = sequence.next_by_code("mobipine_project.hr_function") or "New"
        return super().create(vals_list)

    def _compute_task_count(self):
        task_model = self.env["project.task"].sudo()
        for record in self:
            record.task_count = task_model.search_count([("hr_function_id", "=", record.id)])

    @api.depends_context("project_id")
    def _compute_project_task_count(self):
        """Count tasks for this HR function scoped to the project in context.

        When rendered inside the project form (context has 'project_id'), only
        tasks belonging to that project are counted.  Falls back to the global
        count when no project context is present.
        """
        task_model = self.env["project.task"].sudo()
        project_id = self.env.context.get("project_id")
        for record in self:
            domain = [("hr_function_id", "=", record.id)]
            if project_id:
                domain.append(("project_id", "=", project_id))
            record.project_task_count = task_model.search_count(domain)

    def action_view_tasks(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("project.action_view_task")
        action["domain"] = [("hr_function_id", "=", self.id)]
        action["context"] = {
            "default_hr_function_id": self.id,
            "search_default_hr_function_id": self.id,
        }
        return action

    def action_view_tasks_in_project(self):
        """Open tasks for this HR function filtered to the project in context."""
        self.ensure_one()
        project_id = self.env.context.get("project_id")
        action = self.env["ir.actions.actions"]._for_xml_id("project.action_view_task")
        action["domain"] = [("hr_function_id", "=", self.id)]
        action["context"] = {
            "default_hr_function_id": self.id,
        }
        if project_id:
            action["domain"].append(("project_id", "=", project_id))
            action["context"]["default_project_id"] = project_id
            action["context"]["search_default_project_id"] = project_id
        return action
