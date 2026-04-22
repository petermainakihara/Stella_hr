from odoo import api, fields, models


class StellarTaskFeedback(models.Model):
    _name = "stellar.task.feedback"
    _description = "Task Feedback (Immutable)"
    _order = "create_date desc"
    _log_access = False

    task_id = fields.Many2one(
        "project.task",
        required=True,
        ondelete="cascade",
        index=True,
    )
    author_id = fields.Many2one(
        "res.users",
        required=True,
        default=lambda self: self.env.user,
        readonly=True,
    )
    comment = fields.Text(required=True, help="Assignee feedback on task completion.")
    create_date = fields.Datetime(readonly=True, default=fields.Datetime.now)

    _sql_constraints = [
        (
            "stellar_task_feedback_one_per_user_per_task",
            "UNIQUE(task_id, author_id)",
            "Only one feedback per user per task. Update the existing record instead.",
        )
    ]

    def unlink(self):
        """Immutable — feedback cannot be deleted."""
        raise models.ValidationError(
            "Feedback records are immutable and cannot be deleted. "
            "Contact system administrator to modify."
        )
