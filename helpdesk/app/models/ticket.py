from app import db
from app.models.base_entity import BaseEntity

class Ticket(BaseEntity, db.Model):

    __tablename__ = "tickets"

    # Base Columns
    ticket_id = db.Column("ticketid", db.Integer, primary_key=True)
    title = db.Column("title", db.String(255), nullable=False)
    description = db.Column("description", db.Text, nullable=False)
    status = db.Column("status", db.String(255), nullable=False)
    due_date = db.Column("duedate", db.Date, nullable=False) # derived from priority.delay_hours (?)
    
    # Foreign Keys
    user_id = db.Column("userid", db.Integer, db.ForeignKey("users.userid"), nullable=False)
    category_id = db.Column("categoryid", db.Integer, db.ForeignKey("categories.categoryid"), nullable=False)
    priority_id = db.Column("priorityid", db.Integer, db.ForeignKey("priorities.priorityid"), nullable=False)
    equipment_id = db.Column("equipmentid", db.Integer, db.ForeignKey("equipments.equipmentid"), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="tickets")
    category = db.relationship("Category", back_populates="tickets")
    priority = db.relationship("Priority", back_populates="tickets")
    equipment = db.relationship("Equipment", back_populates="tickets")
    

    def __repr__(self):
        return f"<Ticket ['{self.title}' ID: {self.ticket_id}]>"

