from app import db
from app.models.base_entity import BaseEntity
from app.models.equipment import Equipment
from app.models.user import User


class Site(BaseEntity, db.Model):
    __tablename__ = "sites"

    # --- Colonnes -----------------------------------------------------

    site_id = db.Column("siteid", db.Integer, primary_key=True)
    name = db.Column("sitename", db.String(50), unique=True, index=True)
    address = db.Column("siteaddress", db.Text)
    city = db.Column("sitecity", db.String(50))

    # --- Relations -----------------------------------------------------
    users = db.relationship("User", back_populates="site")
    equipments = db.relationship("Equipment", back_populates="site")

    def add_user(self, user: User):
        if user.user_id in self.user_ids():
            return

        self.users.append(user)

    def remove_user(self, user: User):
        if user.user_id not in self.user_ids():
            return

        self.users.remove(user)

    def add_equipment(self, equipment: Equipment):
        if equipment.serial in self.equipment_serials():
            return 

        self.equipments.append(equipment)

    def user_names(self) -> list[str]:
        return [user.name for user in self.users]

    def user_ids(self) -> list[int]:
        return [user.user_id for user in self.users]

    def equipment_serials(self) -> list[str]:
        return [equipment.serial for equipment in self.equipments]

    def __repr__(self):
        return f"<Site {self.site_id}: {self.name}>"
