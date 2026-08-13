from app.models.priority import Priority
from datetime import timedelta, datetime
from sqlalchemy.exc import SQLAlchemyError
from app import app, db
from app.dtos.ticket_dto import TicketDTO
from app.forms.tickets.ticket_form import TicketForm
from app.mappers.ticket_mapper import TicketMapper
from app.models.ticket import Ticket
from app.framework.service import AbstractService

class TicketService(AbstractService):
    def insert(self, form: TicketForm) -> TicketDTO | None:
        try:
            ticket = Ticket()
            TicketMapper.form_to_entity(form, ticket)

            # Set current user as author
            # Temporary: Set the first user in db as author
            ticket.author_id = 1
            # Set status to "New" by default
            ticket.status = "New"

            # Compute due date (now + (priority delay in hours))
            delay = Priority.query.get(ticket.priority_id).delay_hours
            ticket.due_date = datetime.now() + timedelta(hours=delay)

            db.session.add(ticket)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            app.logger.error(f"Erreur lors de la création du ticket: {e}")
            return None
        else:
            return TicketMapper.entity_to_dto(ticket)

    def find_all(self):
        pass

    def find_one(self, entity_id: int):
        pass

    def find_one_by(self, **kwargs):
        pass

    def find_one_entity(self, entity_id: int):
        pass

    def update(self, entity_id: int, data):
        pass

    def delete(self, entity_id: int):
        pass