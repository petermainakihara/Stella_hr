from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["res.partner"].search([
        ("attendance_radius_km", "<", 30.0),
    ]).write({"attendance_radius_km": 30.0})