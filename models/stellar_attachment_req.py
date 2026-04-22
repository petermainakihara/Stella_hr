from odoo import api, fields, models


class StellarAttachmentReq(models.Model):
    _name = "stellar.attachment.req"
    _description = "Required Attachment Slot"
    _order = "sequence, id"

    task_id = fields.Many2one(
        "project.task",
        required=True,
        ondelete="cascade",
        index=True,
    )
    label = fields.Char(
        required=True,
        help="Human-readable slot name, e.g. 'Signed SLA'.",
    )
    sequence = fields.Integer(default=10)
    attachment_id = fields.Many2one(
        "ir.attachment",
        string="Attachment",
        help="Fulfilled when this attachment is linked.",
    )
    expected_doc_type_id = fields.Many2one(
        "stellar.document.type",
        string="Expected Document Type",
        help="If set, the uploaded file must match this type.",
    )
    is_fulfilled = fields.Boolean(
        compute="_compute_is_fulfilled",
        store=True,
        string="Fulfilled",
        help="True when attachment is linked and type matches (if required).",
    )

    @api.depends("attachment_id", "attachment_id.doc_type_id", "expected_doc_type_id")
    def _compute_is_fulfilled(self):
        """Check if attachment slot is fulfilled."""
        for record in self:
            if not record.attachment_id:
                record.is_fulfilled = False
                continue
            # If a doc type is expected, verify match
            if record.expected_doc_type_id:
                record.is_fulfilled = (
                    record.attachment_id.doc_type_id == record.expected_doc_type_id
                )
            else:
                record.is_fulfilled = True
