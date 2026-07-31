from app import db
from app.models.base_entity import BaseEntity


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

    def __repr__(self):
        return f"<Site {self.site_id}: {self.name}>"
