from odoo import fields, models


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    def write(self, vals):
        open_attendances = self.filtered(lambda attendance: not attendance.check_out)
        result = super().write(vals)

        if "check_out" in vals:
            checkout_time = vals.get("check_out") or fields.Datetime.now()
            sessions = self.env["mobipine_project.checkin_session"].search(
                [
                    ("attendance_id", "in", open_attendances.ids),
                    ("state", "=", "open"),
                ]
            )
            if sessions:
                sessions.action_close_session(check_out_time=checkout_time)

        return result