from app.framework.mapper import AbstractMapper
from app.dtos.ticket_dto import TicketDTO
from app.models.ticket import Ticket

class TicketMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(ticket: Ticket) -> TicketDTO:
        return TicketDTO.build_from_entity(ticket)
    
    @staticmethod
    def form_to_entity(form, ticket: Ticket) -> Ticket:
        ticket.title = form.title.data
        ticket.description = form.description.data
        ticket.status = form.status.data
        ticket.due_date = form.due_date.data
        ticket.author_id = form.author_id.data
        ticket.technician_id = form.technician_id.data
        ticket.category_id = form.category_id.data
        ticket.priority_id = form.priority_id.data
        ticket.equipment_id = form.equipment_id.data
        return ticket
