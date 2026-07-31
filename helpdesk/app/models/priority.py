from app import db
from app.models.base_entity import BaseEntity

class Priority(BaseEntity, db.Model):

    __tablename__ = "priorities"

    priority_id = db.Column("priorityid", db.Integer, primary_key=True)
    name = db.Column("priorityname", db.String(255), nullable=False, index=True, unique=True)
    level = db.Column("prioritylevel", db.Integer, nullable=False)
    delay_hours = db.Column("prioritydelayhours", db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<Priority ['{self.name}' ID: {self.priority_id}]>"