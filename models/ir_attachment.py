from odoo import models, fields, api


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    doc_type_id = fields.Many2one(
        "stellar.document.type",
        string="Document Type",
        help="Classification of this document for reporting and compliance.",
    )

    def get_documents_operation_add_destination(self):
        """Auto-move chatter attachments to task folder (FR-DOC-07)."""
        self.ensure_one()

        if self.res_model == "project.task":
            task = self.env["project.task"].browse(self.res_id)
            if task.exists():
                if task.documents_folder_id:
                    return {
                        "display_name": task.documents_folder_id.display_name,
                    }
                if task.project_id and task.project_id.documents_folder_id:
                    return {
                        "destination": str(task.project_id.documents_folder_id.id),
                        "display_name": task.project_id.documents_folder_id.display_name,
                    }

        if self.res_model == "project.project":
            project = self.env["project.project"].browse(self.res_id)
            if project.exists() and project.documents_folder_id:
                return {
                    "destination": str(project.documents_folder_id.id),
                    "display_name": project.documents_folder_id.display_name,
                }

        return super().get_documents_operation_add_destination()
