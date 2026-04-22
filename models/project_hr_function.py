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
