from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProjectTaskTemplate(models.Model):
    _name = "mobipine_project.task_template"
    _description = "Recurring Task Template"
    _order = "sequence, id"

    name = fields.Char(required=True)
    code = fields.Char(default="New", copy=False, readonly=True, index=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    description = fields.Html()
    hr_function_id = fields.Many2one(
        "mobipine_project.hr_function",
        required=True,
        ondelete="cascade",
        index=True,
    )
    sla_id = fields.Many2one(
        "mobipine_project.sla",
        related="hr_function_id.sla_id",
        store=True,
        readonly=True,
        index=True,
    )
    recurrence_rule = fields.Selection(
        selection=[
            ("none", "None"),
            ("daily", "Daily"),
            ("weekly", "Weekly"),
            ("monthly", "Monthly"),
        ],
        default="monthly",
        required=True,
        index=True,
    )
    next_spawn_date = fields.Date(index=True)
    required_attachment_def = fields.Text(
        help="Optional JSON/text definition used in later phases for completion gating.",
    )

    _sql_constraints = [
        (
            "mobipine_project_task_template_name_function_uniq",
            "unique(name, hr_function_id)",
            "Task template name must be unique per HR Function.",
        ),
        (
            "mobipine_project_task_template_code_uniq",
            "unique(code)",
            "Task template code must be unique.",
        ),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        sequence = self.env["ir.sequence"]
        for vals in vals_list:
            if vals.get("code", "New") == "New":
                vals["code"] = sequence.next_by_code("mobipine_project.task_template") or "New"
        records = super().create(vals_list)
        for record in records.filtered(lambda r: r.recurrence_rule != "none" and not r.next_spawn_date):
            record.next_spawn_date = fields.Date.context_today(record)
        return records

    @api.constrains("recurrence_rule", "next_spawn_date")
    def _check_recurrence_dates(self):
        for record in self:
            if record.recurrence_rule != "none" and not record.next_spawn_date:
                raise ValidationError("A recurring template must have a next spawn date.")

    @api.model
    def _next_cycle_date(self, recurrence_rule, current_date):
        if recurrence_rule == "daily":
            return current_date + relativedelta(days=1)
        if recurrence_rule == "weekly":
            return current_date + relativedelta(weeks=1)
        if recurrence_rule == "monthly":
            return current_date + relativedelta(months=1)
        return current_date

    @api.model
    def cron_spawn_tasks_from_templates(self):
        today = fields.Date.context_today(self)
        templates = self.search(
            [
                ("active", "=", True),
                ("recurrence_rule", "!=", "none"),
                ("next_spawn_date", "<=", today),
            ]
        )

        task_model = self.env["project.task"]
        log_model = self.env["mobipine_project.spawn_log"]

        for template in templates:
            projects = self.env["project.project"].search(
                [
                    ("active", "=", True),
                    ("sla_id", "=", template.sla_id.id),
                ]
            )

            for project in projects:
                existing = task_model.search_count(
                    [
                        ("project_id", "=", project.id),
                        ("task_template_id", "=", template.id),
                        ("cycle_date", "=", template.next_spawn_date),
                    ]
                )
                if existing:
                    log_model.create(
                        {
                            "template_id": template.id,
                            "project_id": project.id,
                            "cycle_date": template.next_spawn_date,
                            "status": "skipped",
                            "message": "Task already exists for this template/project/cycle.",
                        }
                    )
                    continue

                vals = {
                    "name": "%s - %s" % (template.hr_function_id.name, template.name),
                    "project_id": project.id,
                    "description": template.description or False,
                    "task_template_id": template.id,
                    "hr_function_id": template.hr_function_id.id,
                    "cycle_date": template.next_spawn_date,
                    "spawned_by_cron": True,
                }
                if project.user_id:
                    vals["user_ids"] = [(4, project.user_id.id)]

                try:
                    task = task_model.create(vals)
                    log_model.create(
                        {
                            "template_id": template.id,
                            "project_id": project.id,
                            "task_id": task.id,
                            "cycle_date": template.next_spawn_date,
                            "status": "spawned",
                            "message": "Task created successfully.",
                        }
                    )
                except Exception as error_message:
                    log_model.create(
                        {
                            "template_id": template.id,
                            "project_id": project.id,
                            "cycle_date": template.next_spawn_date,
                            "status": "error",
                            "message": str(error_message),
                        }
                    )

            template.next_spawn_date = self._next_cycle_date(template.recurrence_rule, template.next_spawn_date)
