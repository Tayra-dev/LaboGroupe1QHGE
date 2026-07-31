from app import db
from app.models.base_entity import BaseEntity


class Equipment(BaseEntity, db.Model):
    """Un équipement du parc matériel."""

    __tablename__ = "equipments"

    equipment_id = db.Column("equipmentid", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("equipmentname", db.String(50))
    type = db.Column("equipmenttype", db.String(50))
    serial = db.Column("equipmentserial", db.String(50), unique=True)
    purchase_date = db.Column("equipmentpurchasedate", db.Date)

    site_id = db.Column("siteid", db.ForeignKey("sites.siteid"))
    user_id = db.Column("userid", db.ForeignKey("users.userid"), nullable=True)
    
    site = db.relationship("sites", back_populates="equipments")
    user = db.relationship("users", back_populates="equipments")

    def __repr__(self):
        return f"<Equipment {self.equipment_id}: {self.name}>"