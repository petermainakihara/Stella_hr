import logging

from odoo import http
from odoo.addons.web.controllers.action import Action as WebAction
from odoo.exceptions import AccessError
from odoo.http import request

_logger = logging.getLogger(__name__)


class StellarCheckinRequiredError(AccessError):
    """Raised when a user without an open check-in session tries to load
    a blocked action. Carries a distinct name so the frontend can detect
    it reliably and show the check-in modal instead of a generic error."""


class Action(WebAction):
    def _stellar_get_employee(self):
        employee = request.env["hr.employee"].sudo().search(
            [("user_id", "=", request.env.user.id)],
            limit=1,
            order="id desc",
        )
        return employee or False

    def _stellar_has_open_attendance(self):
        employee = self._stellar_get_employee()
        if not employee:
            return False
        return bool(
            request.env["mobipine_project.checkin_session"].search(
                [
                    ("employee_id", "=", employee.id),
                    ("state", "=", "open"),
                ],
                limit=1,
            )
        )

    def _stellar_is_settings_action(self, action, xmlid):
        if xmlid and (
            xmlid.startswith("base_setup.")
            or xmlid.startswith("base.")
            and "settings" in xmlid
            or xmlid == "base.action_general_settings"
        ):
            return True
        res_model = getattr(action, "res_model", False)
        return res_model == "res.config.settings"

    def _stellar_action_is_allowed(self, action):
        if request.env.user.has_group("base.group_system"):
            _logger.warning("STELLAR GATE: user=%s is admin, allowing", request.env.user.login)
            return True

        if self._stellar_has_open_attendance():
            _logger.warning("STELLAR GATE: user=%s has open checkin session, allowing", request.env.user.login)
            return True

        xmlid = action.get_external_id().get(action.id)
        res_model = getattr(action, "res_model", False)

        if xmlid and xmlid.startswith("hr_attendance."):
            _logger.warning("STELLAR GATE: xmlid=%s is hr_attendance, allowing", xmlid)
            return True

        if xmlid == "mobipine_odoo_project_management.action_attendance_checkin_wizard":
            _logger.warning("STELLAR GATE: xmlid=%s is checkin wizard, allowing", xmlid)
            return True

        if res_model == "hr.attendance":
            _logger.warning("STELLAR GATE: res_model=hr.attendance, allowing")
            return True

        if self._stellar_is_settings_action(action, xmlid):
            _logger.warning("STELLAR GATE: xmlid=%s is settings action, allowing", xmlid)
            return True

        _logger.warning(
            "STELLAR GATE: xmlid=%s res_model=%s BLOCKED for user=%s",
            xmlid, res_model, request.env.user.login,
        )
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
        _logger.warning(
            "STELLAR GATE: load() ENTERED with action_id=%s, user=%s",
            action_id, request.env.user.login,
        )
        action = self._stellar_get_action_record(action_id)
        if action and not self._stellar_action_is_allowed(action):
            _logger.warning(
                "STELLAR GATE: RAISING StellarCheckinRequiredError for action_id=%s, user=%s",
                action_id, request.env.user.login,
            )
            raise StellarCheckinRequiredError("STELLAR_CHECKIN_REQUIRED")
        return super().load(action_id, context=context)

    @http.route("/web/stellar/check_session", type="jsonrpc", auth="user", readonly=True)
    def check_session(self):
        """Called on frontend startup to check if current user has an open
        check-in session. Used by the proactive gate to catch existing users
        who bypass the reactive error handler via cached browser state."""
        try:
            if request.env.user.has_group("base.group_system"):
                return {"has_session": True}
            employee = self._stellar_get_employee()
            if not employee:
                # No employee record linked — must check in first
                return {"has_session": False}
            has_session = bool(
                request.env["mobipine_project.checkin_session"].search(
                    [
                        ("employee_id", "=", employee.id),
                        ("state", "=", "open"),
                    ],
                    limit=1,
                )
            )
            return {"has_session": has_session}
        except Exception as e:
            _logger.error("STELLAR check_session error: %s", e)
            # Fail closed — if we can't check, block access
            return {"has_session": False}