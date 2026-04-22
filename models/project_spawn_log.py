from odoo import fields, models


class ProjectSpawnLog(models.Model):
    _name = "mobipine_project.spawn_log"
    _description = "Recurring Task Spawn Log"
    _order = "create_date desc, id desc"

    template_id = fields.Many2one("mobipine_project.task_template", required=True, ondelete="cascade", index=True)
    project_id = fields.Many2one("project.project", required=True, ondelete="cascade", index=True)
    task_id = fields.Many2one("project.task", ondelete="set null", index=True)
    cycle_date = fields.Date(required=True, index=True)
    status = fields.Selection(
        selection=[("spawned", "Spawned"), ("skipped", "Skipped"), ("error", "Error")],
        required=True,
        index=True,
    )
    message = fields.Text()
