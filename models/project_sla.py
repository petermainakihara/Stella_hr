from odoo import api, fields, models


class ProjectSLA(models.Model):
    _name = "mobipine_project.sla"
    _description = "Client SLA"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    name = fields.Char(required=True, tracking=True)
    code = fields.Char(default="New", copy=False, readonly=True, index=True)
    client_type = fields.Selection(
        selection=[("one_off", "One-off"), ("retainer", "Retainer")],
        required=True,
        default="retainer",
        tracking=True,
    )
    company_id = fields.Many2one(
        "res.company",
        required=True,
        default=lambda self: self.env.company,
        index=True,
    )
    active = fields.Boolean(default=True)
    partner_ids = fields.Many2many(
        "res.partner",
        "mobipine_project_sla_partner_rel",
        "sla_id",
        "partner_id",
        string="Clients",
    )
    hr_function_ids = fields.One2many(
        "mobipine_project.hr_function",
        "sla_id",
        string="HR Functions",
    )

    _sql_constraints = [
        (
            "mobipine_project_sla_code_company_uniq",
            "unique(code, company_id)",
            "SLA code must be unique per company.",
        ),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        sequence = self.env["ir.sequence"]
        for vals in vals_list:
            if vals.get("code", "New") == "New":
                vals["code"] = sequence.next_by_code("mobipine_project.sla") or "New"
        return super().create(vals_list)
