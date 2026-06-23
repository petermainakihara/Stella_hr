from odoo import models


class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    def _stellar_get_user_employee(self):
        user = self.env.user
        employee = getattr(user, "employee", False)
        if employee:
            return employee
        employee = getattr(user, "employee_id", False)
        if employee:
            return employee
        employees = getattr(user, "employee_ids", False)
        return employees[:1] if employees else False