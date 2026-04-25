from odoo import models


class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    def _load_menus_blacklist(self):
        blacklist = super()._load_menus_blacklist()
        if not self.env.user.has_group("base.group_system"):
            employee = self.env.user.employee_id or self.env.user.employee_ids[:1]
            if employee and employee._stellar_get_open_attendance():
                return blacklist

            attendance_root = self.env.ref(
                "hr_attendance.menu_hr_attendance_root",
                raise_if_not_found=False,
            )
            root_menus = self.sudo().search([("parent_id", "=", False)])
            for menu in root_menus:
                if not attendance_root or menu.id != attendance_root.id:
                    blacklist.append(menu.id)
        return blacklist