from app.framework.mapper.abstract_mapper import AbstractMapper
from app.dtos.attachment_dto import AttachmentDTO
from app.forms.attachment_form import AttachmentForm
from app.models.attachment import Attachment
from app import os


class AttachmentMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(attachment: Attachment) -> AttachmentDTO:
        return AttachmentDTO.build_from_entity(attachment)

    @staticmethod
    def form_to_entity(form, attachment: Attachment, author_id: int, ticket_id: int, attachment_path: str) -> Attachment:
        if isinstance(form, AttachmentForm):
            file_data = form.attachment.data

            if file_data:
                attachment.attachment_filename = file_data.filename 
                attachment.attachment_path = attachment_path

                file_data.seek(0, os.SEEK_END)
                attachment.attachment_size = file_data.tell()
                file_data.seek(0)

                attachment.ticket_id = ticket_id
                attachment.author_id = author_id

        return attachment