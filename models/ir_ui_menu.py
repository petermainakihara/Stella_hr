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

    def _load_menus_blacklist(self):
        blacklist = list(super()._load_menus_blacklist())
        if not self.env.user.has_group("base.group_system"):
            employee = self._stellar_get_user_employee()
            if not employee:
                return blacklist
            if employee and employee._stellar_get_open_attendance():
                return blacklist

            has_attendance_access = self.env.user.has_group("hr_attendance.group_hr_attendance_user") or self.env.user.has_group(
                "hr_attendance.group_hr_attendance_manager"
            )
            attendance_root = self.env.ref(
                "hr_attendance.menu_hr_attendance_root",
                raise_if_not_found=False,
            )
            if not attendance_root or not has_attendance_access:
                return blacklist

            root_menus = self.sudo().search([("parent_id", "=", False)])
            for menu in root_menus:
                if menu.id != attendance_root.id:
                    blacklist.append(menu.id)
        return list(dict.fromkeys(blacklist))