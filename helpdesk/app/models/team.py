from app import db
from app.models.base_entity import BaseEntity


class Team(BaseEntity, db.Model):
    """Une équipe de support"""

    __tablename__ = "teams"

    # --- Colonnes -----------------------------------------------------

    team_id = db.Column("teamid", db.Integer, primary_key=True)
    name = db.Column("teamname", db.String, unique=True, index=True)
    description = db.Column("teamdescription", db.String, nullable=True)

    # --- Relations -----------------------------------------------------

    members = db.relationship("User", back_populates="team")
