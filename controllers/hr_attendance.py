from odoo import fields, http
from odoo.addons.hr_attendance.controllers.main import HrAttendance as HrAttendanceController
from odoo.tools import float_round
from odoo.tools.image import image_data_uri
from odoo.http import request


class HrAttendance(HrAttendanceController):
    @staticmethod
    def _stellar_get_user_employee():
        employee = request.env["hr.employee"].sudo().search(
            [("user_id", "=", request.env.user.id)],
            limit=1,
            order="id desc",
        )
        if employee:
            return employee
        user = request.env.user
        employee = getattr(user, "employee", False) or getattr(user, "employee_id", False)
        if employee:
            return employee
        employees = getattr(user, "employee_ids", False)
        return employees[:1] if getattr(employees, "_name", None) == "hr.employee" and employees else False

    @staticmethod
    def _stellar_get_user_attendance_data(employee):
        response = {}
        if employee:
            response = {
                "id": employee.id,
                "hours_today": float_round(employee.hours_today, precision_digits=2),
                "hours_previously_today": float_round(employee.hours_previously_today, precision_digits=2),
                "last_attendance_worked_hours": float_round(employee.last_attendance_worked_hours, precision_digits=2),
                "last_check_in": employee.last_check_in,
                "attendance_state": employee.attendance_state,
                "display_systray": employee.company_id.attendance_from_systray,
                "device_tracking_enabled": employee.company_id.attendance_device_tracking,
            }
        return response

    @staticmethod
    def _stellar_get_employee_info_response(employee):
        response = {}
        if employee:
            response = {
                **HrAttendance._stellar_get_user_attendance_data(employee),
                "employee_name": employee.name,
                "employee_avatar": employee.image_256 and image_data_uri(employee.image_256),
                "total_overtime": float_round(employee.total_overtime, precision_digits=2),
                "kiosk_delay": employee.company_id.attendance_kiosk_delay * 1000,
                "attendance": {
                    "check_in": employee.last_attendance_id.check_in,
                    "check_out": employee.last_attendance_id.check_out,
                },
                "overtime_today": sum(
                    request.env["hr.attendance.overtime.line"].sudo().search([
                        ("employee_id", "=", employee.id),
                        ("date", "=", fields.Date.today()),
                    ]).mapped("duration")
                )
                or 0,
                "use_pin": employee.company_id.attendance_kiosk_use_pin,
                "display_overtime": employee.company_id.hr_attendance_display_overtime,
                "device_tracking_enabled": employee.company_id.attendance_device_tracking,
            }
        return response

    @http.route("/hr_attendance/attendance_user_data", type="jsonrpc", auth="user", readonly=True)
    def user_attendance_data(self):
        employee = self._stellar_get_user_employee()
        return self._stellar_get_user_attendance_data(employee)

    @http.route("/hr_attendance/systray_check_in_out", type="jsonrpc", auth="user")
    def systray_attendance(self, latitude=False, longitude=False):
        employee = self._stellar_get_user_employee()
        if not employee:
            return self._stellar_get_user_attendance_data(False)
        geo_ip_response = self._get_geoip_response(
            mode="systray",
            latitude=latitude,
            longitude=longitude,
            device_tracking_enabled=employee.company_id.attendance_device_tracking,
        )
        employee._attendance_action_change(geo_ip_response)
        return self._stellar_get_employee_info_response(employee)