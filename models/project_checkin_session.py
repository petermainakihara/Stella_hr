from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProjectCheckinSession(models.Model):
    _name = "mobipine_project.checkin_session"
    _description = "Project Check-in Session"
    _order = "check_in_time desc, id desc"

    user_id = fields.Many2one("res.users", required=True, index=True, default=lambda self: self.env.user)
    project_id = fields.Many2one("project.project", required=True, index=True, ondelete="cascade")
    check_in_time = fields.Datetime(required=True, default=fields.Datetime.now, index=True)
    check_out_time = fields.Datetime()
    state = fields.Selection(
        selection=[("open", "Open"), ("closed", "Closed")],
        default="open",
        required=True,
        index=True,
    )
    geo_lat = fields.Float(digits=(16, 8))
    geo_lng = fields.Float(digits=(16, 8))
    duration_hours = fields.Float(compute="_compute_duration_hours", store=True)

    _sql_constraints = [
        (
            "mobipine_project_checkin_time_order",
            "check(check_out_time IS NULL OR check_out_time >= check_in_time)",
            "Check-out time cannot be before check-in time.",
        )
    ]

    @api.depends("check_in_time", "check_out_time", "state")
    def _compute_duration_hours(self):
        for record in self:
            if not record.check_in_time:
                record.duration_hours = 0.0
                continue
            end_time = record.check_out_time or fields.Datetime.now()
            record.duration_hours = max((end_time - record.check_in_time).total_seconds() / 3600.0, 0.0)

    @api.constrains("state", "user_id")
    def _check_single_open_session(self):
        for record in self.filtered(lambda r: r.state == "open"):
            domain = [
                ("id", "!=", record.id),
                ("state", "=", "open"),
                ("user_id", "=", record.user_id.id),
            ]
            if self.search_count(domain):
                raise ValidationError("Only one open check-in session is allowed per user globally.")

    def action_close_session(self):
        for record in self.filtered(lambda r: r.state == "open"):
            record.write(
                {
                    "state": "closed",
                    "check_out_time": fields.Datetime.now(),
                }
            )
