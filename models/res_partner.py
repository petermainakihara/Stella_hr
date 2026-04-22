from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    client_type = fields.Selection(
        selection=[("one_off", "One-off"), ("retainer", "Retainer")],
        string="Client Type",
        groups="mobipine_odoo_project_management.group_project_manager,base.group_system",
        tracking=True,
    )
    sla_ids = fields.Many2many(
        "mobipine_project.sla",
        "mobipine_project_sla_partner_rel",
        "partner_id",
        "sla_id",
        string="SLAs",
        groups="mobipine_odoo_project_management.group_project_manager,base.group_system",
    )
