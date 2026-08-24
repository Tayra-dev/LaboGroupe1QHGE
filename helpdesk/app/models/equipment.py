from app import db
from app.models.base_entity import BaseEntity


class Equipment(BaseEntity, db.Model):
    """Un équipement du parc matériel."""

    __tablename__ = "equipments"

    equipment_id = db.Column("equipmentid", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("equipmentname", db.String(50), nullable=False)
    type = db.Column("equipmenttype", db.String(50), nullable=False)
    serial = db.Column("equipmentserial", db.String(50), unique=True)
    purchase_date = db.Column("equipmentpurchasedate", db.Date, nullable=False)

    site_id = db.Column("siteid", db.ForeignKey("sites.siteid"), nullable=False)
    user_id = db.Column("userid", db.ForeignKey("users.userid"))
    
    site = db.relationship("Site", back_populates="equipments")
    user = db.relationship("User", back_populates="equipments")
    ticket = db.relationship("Ticket", back_populates="equipment")


    def add_user(self, user):
            if user.user_id == self.user_id or self.user_id is not None:
                return
    
            self.user = user
    
    def remove_user(self, user):
        if user.user_id != self.user_id:
            return

        self.user = None

    def add_site(self, site):
        if site.site_id == self.site_id or self.site_id is not None:
            return 

        self.site = site

    def __repr__(self):
        return f"<Equipment {self.equipment_id}: {self.name}>"