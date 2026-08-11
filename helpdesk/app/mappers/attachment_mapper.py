from app.mappers.abstract_mapper import AbstractMapper
from app.dtos.attachment_dto import AttachmentDTO
from app.models.attachment import Attachment


class AttachmentMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(attachment: Attachment) -> AttachmentDTO:
        return AttachmentDTO.build_from_entity(attachment)

    #creation de l'attachement géré par le service