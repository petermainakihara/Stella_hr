from odoo import api, fields, models
from odoo.exceptions import UserError


class StellarTaskProgress(models.Model):
    _name = "stellar.task.progress"
    _description = "Task Progress Record (User-Linked)"
    _order = "create_date desc"

    task_id = fields.Many2one(
        "project.task",
        required=True,
        ondelete="cascade",
        index=True,
    )
    user_id = fields.Many2one(
        "res.users",
        required=True,
        default=lambda self: self.env.user,
        readonly=True,
    )
    progress_pct = fields.Integer(
        required=True,
        help="Progress percentage (0-100).",
    )
    notes = fields.Text(help="Optional notes on progress.")
    create_date = fields.Datetime(readonly=True, default=fields.Datetime.now)
    write_date = fields.Datetime(readonly=True)

    _sql_constraints = [
        (
            "stellar_task_progress_pct_range",
            "CHECK(progress_pct >= 0 AND progress_pct <= 100)",
            "Progress percentage must be between 0 and 100.",
        )
    ]

    @api.model_create_multi
    def create(self, vals_list):
        """Track creation timestamp and enforce author linkage."""
        for vals in vals_list:
            vals["user_id"] = self.env.user.id
            if "create_date" not in vals:
                vals["create_date"] = fields.Datetime.now()
        return super().create(vals_list)

    def write(self, vals):
        if "user_id" in vals:
            raise UserError("Progress author cannot be changed after creation.")

        if not self.env.user.has_group("base.group_system"):
            unauthorized = self.filtered(lambda record: record.user_id.id != self.env.user.id)
            if unauthorized:
                raise UserError("You can only update progress records that you created.")

        return super().write(vals)

    def unlink(self):
        if not self.env.user.has_group("base.group_system"):
            unauthorized = self.filtered(lambda record: record.user_id.id != self.env.user.id)
            if unauthorized:
                raise UserError("You can only delete progress records that you created.")
        return super().unlink()
