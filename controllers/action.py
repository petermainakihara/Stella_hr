from odoo import http
from odoo.addons.web.controllers.action import Action as WebAction
from odoo.exceptions import AccessError
from odoo.http import request


class Action(WebAction):
    def _stellar_has_open_attendance(self):
        employee = request.env.user.employee_id or request.env.user.employee_ids[:1]
        return bool(employee and employee._stellar_get_open_attendance())

    def _stellar_action_is_allowed(self, action):
        if request.env.user.has_group("base.group_system"):
            return True
        if self._stellar_has_open_attendance():
            return True

        xmlid = action.get_external_id().get(action.id)
        if xmlid and xmlid.startswith("hr_attendance."):
            return True

        if xmlid == "mobipine_odoo_project_management.action_attendance_checkin_wizard":
            return True

        return False

    def _stellar_get_action_record(self, action_id):
        action_model = request.env["ir.actions.actions"]
        if isinstance(action_id, str):
            action = request.env.ref(action_id, raise_if_not_found=False)
            if action:
                return action
            if action_id.isdigit():
                return action_model.browse(int(action_id)).exists()
            return action_model.browse([])
        return action_model.browse(action_id).exists()

    @http.route("/web/action/load", type="jsonrpc", auth="user", readonly=True)
    def load(self, action_id, context=None):
        action = self._stellar_get_action_record(action_id)
        if action and not self._stellar_action_is_allowed(action):
            raise AccessError("You must check in before opening apps.")
        return super().load(action_id, context=context)