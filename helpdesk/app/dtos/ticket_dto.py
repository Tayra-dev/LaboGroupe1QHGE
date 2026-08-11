from app.dtos.abstract_dto import AbstractDTO
from app.models.ticket import Ticket


class TicketDTO(AbstractDTO):
    
    def __init__(self):
        self.ticket_id = None
        self.ticket_title = None
        self.ticket_description = None
        self.ticket_status = None
        self.ticket_due_date = None
        self.ticket_author_id = None
        self.ticket_technician_id = None
        self.ticket_category = None
        self.ticket_priority = None
        self.ticket_comments = []
        self.ticket_attachments = []
        self.ticket_status_history = []

    @staticmethod
    def build_from_entity(ticket: Ticket) -> "TicketDTO":
        ticket_dto = TicketDTO()

        ticket_dto.ticket_id = ticket.ticket_id
        ticket_dto.ticket_name = ticket.name
        ticket_dto.ticket_description = ticket.description
        ticket_dto.ticket_status = ticket.status
        ticket_dto.ticket_priority = ticket.priority
        ticket_dto.ticket_category = ticket.category
        ticket_dto.ticket_assignee = ticket.assignee
        ticket_dto.ticket_reporter = ticket.reporter
        ticket_dto.ticket_created_at = ticket.created_at
        ticket_dto.ticket_updated_at = ticket.updated_at
        ticket_dto.ticket_closed_at = ticket.closed_at
        ticket_dto.ticket_comments = [CommentDTO.build_from_entity(comment)
                                      for comment in ticket.comments]
        ticket_dto.ticket_attachments = [AttachmentDTO.build_from_entity(attachment)
                                         for attachment in ticket.attachments]
        ticket_dto.ticket_status_history = [TicketStatusHistoryDTO.build_from_entity(status_history)
                                            for status_history in ticket.status_history]

        return ticket_dto
    
    def get_json_parsable(self):
        data = dict(self.__dict__)
        data['ticket_comments'] = [comment.get_json_parsable() for comment in self.ticket_comments]
        data['ticket_attachments'] = [attachment.get_json_parsable() for attachment in self.ticket_attachments]
        data['ticket_status_history'] = [status_history.get_json_parsable() for status_history in self.ticket_status_history]
        return data