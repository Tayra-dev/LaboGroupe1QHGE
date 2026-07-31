from app import db
from app.models.base_entity import BaseEntity
from sqlalchemy import Column, ForeignKey, Integer, String, Text

class SatisfactionSurvey(BaseEntity, db.Model):
    """Une enquête liée à un ticket"""

    __tablename__ = "satisfactionsurveys"

    survey_id = Column("surveyid", Integer, primary_key=True, autoincrement=True)
    rating = Column("surveyrating", Integer)
    comment = Column("surveycomment", Text)

    ticket_id = Column("ticketid", ForeignKey("tickets.ticketid"), unique=True)
    client_id = Column("clientid", ForeignKey("users.userid"))

    ticket = db.relationship("Ticket", back_populates="satisfactionsurveys")
    client = db.relationship("Client", back_populates="satisfactionsurveys")