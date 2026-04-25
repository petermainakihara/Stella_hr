from odoo import fields, models
from odoo.exceptions import UserError


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def _stellar_get_open_attendance(self):
        self.ensure_one()
        return self.env["hr.attendance"].search(
            [
                ("employee_id", "=", self.id),
                ("check_out", "=", False),
            ],
            limit=1,
            order="check_in desc, id desc",
        )

    def _stellar_get_attendance_checkin_action(self, project_id=False, partner_id=False):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "mobipine_odoo_project_management.action_attendance_checkin_wizard"
        )
        action["context"] = {
            "default_employee_id": self.id,
            "default_project_id": project_id,
            "default_partner_id": partner_id,
        }
        return action

    def _stellar_register_attendance_checkin(
        self,
        partner,
        notes,
        geo_lat,
        geo_lng,
        radius_km,
        distance_km,
        project=False,
    ):
        self.ensure_one()
        attendance = self.env["hr.attendance"].create(
            {
                "employee_id": self.id,
                "check_in": fields.Datetime.now(),
            }
        )
        session = self.env["mobipine_project.checkin_session"].create(
            {
                "attendance_id": attendance.id,
                "employee_id": self.id,
                "user_id": self.user_id.id or self.env.user.id,
                "project_id": project.id if project else False,
                "partner_id": partner.id,
                "notes": notes,
                "check_in_time": attendance.check_in,
                "check_in_geo_lat": geo_lat,
                "check_in_geo_lng": geo_lng,
                "check_in_radius_km": radius_km,
                "check_in_distance_km": distance_km,
                "state": "open",
            }
        )
        return attendance, session

    def _stellar_register_attendance_checkout(self):
        self.ensure_one()
        attendance = self._stellar_get_open_attendance()
        if not attendance:
            raise UserError("No open attendance was found for this employee.")

        checkout_time = fields.Datetime.now()
        attendance.write({"check_out": checkout_time})
        session = self.env["mobipine_project.checkin_session"].search(
            [("attendance_id", "=", attendance.id)],
            limit=1,
        )
        if session:
            session.action_close_session(check_out_time=checkout_time)
        return attendance, session

    def attendance_action_change(self):
        self.ensure_one()
        open_attendance = self._stellar_get_open_attendance()
        if open_attendance:
            self._stellar_register_attendance_checkout()
            return True
        return self._stellar_get_attendance_checkin_action()

    def _attendance_action_change(self, geo_information=None):
        self.ensure_one()
        open_attendance = self._stellar_get_open_attendance()
        if open_attendance:
            return self._stellar_register_attendance_checkout()
        return self._stellar_get_attendance_checkin_action()