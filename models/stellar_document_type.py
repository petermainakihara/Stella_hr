from odoo import api, fields, models


class StellarDocumentType(models.Model):
    _name = "stellar.document.type"
    _description = "Document Type"
    _order = "sequence, name"

    name = fields.Char(required=True, help="Display name, e.g. 'SLA Document'.")
    code = fields.Char(
        required=True,
        help="Short code for reporting, e.g. 'SLA', 'CONTRACT', 'PAYSLIP'.",
    )
    description = fields.Text(help="Guidance text shown to users on upload.")
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True, help="Archive flag — archived types hidden from selector.")

    _sql_constraints = [
        (
            "stellar_document_type_name_uniq",
            "UNIQUE(name)",
            "Document type name must be unique.",
        ),
        (
            "stellar_document_type_code_uniq",
            "UNIQUE(code)",
            "Document type code must be unique.",
        )
    ]
