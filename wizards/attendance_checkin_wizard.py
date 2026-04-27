from math import asin, cos, radians, sin, sqrt

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AttendanceCheckinWizard(models.TransientModel):
    _name = "mobipine_project.attendance_checkin_wizard"
    _description = "Attendance Check-in Wizard"

    RADIUS_BUFFER_KM = 2.0

    employee_id = fields.Many2one("hr.employee", required=True, readonly=True)
    project_id = fields.Many2one("project.project", readonly=True)
    partner_id = fields.Many2one("res.partner", required=True)
    notes = fields.Text()
    geo_lat = fields.Float(string="Current Latitude", digits=(16, 8))
    geo_lng = fields.Float(string="Current Longitude", digits=(16, 8))
    client_latitude = fields.Float(related="partner_id.partner_latitude", readonly=True)
    client_longitude = fields.Float(related="partner_id.partner_longitude", readonly=True)
    client_radius_km = fields.Float(related="partner_id.attendance_radius_km", readonly=True)
    distance_km = fields.Float(compute="_compute_distance_km", readonly=True)
    within_radius = fields.Boolean(compute="_compute_distance_km", readonly=True)

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        employee = self.env["hr.employee"].sudo().search(
            [("user_id", "=", self.env.user.id)],
            limit=1,
            order="id desc",
        )
        if not employee:
            user = self.env.user
            employee = getattr(user, "employee", False) or getattr(user, "employee_id", False)
            if not employee:
                employees = getattr(user, "employee_ids", False)
                employee = employees[:1] if getattr(employees, "_name", None) == "hr.employee" and employees else False
        if employee and not res.get("employee_id"):
            res["employee_id"] = employee.id
        if self.env.context.get("default_project_id") and not res.get("project_id"):
            res["project_id"] = self.env.context["default_project_id"]
        if self.env.context.get("default_partner_id") and not res.get("partner_id"):
            res["partner_id"] = self.env.context["default_partner_id"]
        return res

    def _haversine_distance_km(self, lat1, lng1, lat2, lng2):
        earth_radius_km = 6371.0
        delta_lat = radians(lat2 - lat1)
        delta_lng = radians(lng2 - lng1)
        a = sin(delta_lat / 2.0) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(delta_lng / 2.0) ** 2
        return 2.0 * earth_radius_km * asin(sqrt(a))

    def _compute_distance_km(self):
        for record in self:
            if (
                record.geo_lat
                and record.geo_lng
                and record.partner_id
                and record.partner_id.partner_latitude
                and record.partner_id.partner_longitude
            ):
                record.distance_km = record._haversine_distance_km(
                    record.geo_lat,
                    record.geo_lng,
                    record.partner_id.partner_latitude,
                    record.partner_id.partner_longitude,
                )
                record.within_radius = record.distance_km <= record._get_allowed_radius_km()
            else:
                record.distance_km = 0.0
                record.within_radius = False

    def _get_allowed_radius_km(self):
        self.ensure_one()
        return (self.partner_id.attendance_radius_km or 0.0) + self.RADIUS_BUFFER_KM

    def action_confirm_check_in(self):
        self.ensure_one()
        partner = self.partner_id
        if not partner.partner_latitude or not partner.partner_longitude:
            raise ValidationError("The selected client does not have a check-in location configured.")
        if not self.geo_lat or not self.geo_lng:
            raise ValidationError("Your current location is required before check-in can continue.")
        allowed_radius_km = self._get_allowed_radius_km()
        if self.distance_km > allowed_radius_km:
            raise ValidationError(
                "You are %.2f km away from the client premises, which exceeds the allowed radius of %.2f km."
                % (self.distance_km, allowed_radius_km)
            )

        self.employee_id._stellar_register_attendance_checkin(
            partner=partner,
            notes=self.notes,
            geo_lat=self.geo_lat,
            geo_lng=self.geo_lng,
            radius_km=allowed_radius_km,
            distance_km=self.distance_km,
            project=self.project_id,
        )
        return {"type": "ir.actions.client", "tag": "reload"}