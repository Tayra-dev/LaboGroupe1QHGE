from app import db
from app.models.base_entity import BaseEntity
from app.models.role import Role
from app.models.user_role import UserRole


class User(BaseEntity, db.Model):
    """Un utilisateur de la webapp de gestion de tickets."""

    __tablename__ = "users"

    # --- Colonnes ------------------------------------------------------------

    user_id = db.Column("userid", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("username", db.String, unique=True, nullable=False, index=True)
    email = db.Column(
        "useremail", db.String(120), unique=True, nullable=False, index=True
    )
    password = db.Column("userpassword", db.String(255), nullable=False)
    firstname = db.Column("userfirstname", db.String, nullable=False)
    lastname = db.Column("userlastname", db.String, nullable=False)
    team_id = db.Column("teamid", db.ForeignKey("teams.teamid"))
    site_id = db.Column("siteid", db.ForeignKey("sites.siteid"))

    # --- Relations -----------------------------------------------------------

    roles = db.relationship(
        "UserRole", back_populates="rel_user", cascade="all, delete-orphan"
    )
    team = db.relationship("Team", back_populates="members")
    created_tickets = db.relationship(
        "Ticket", foreign_keys="Ticket.author_id", back_populates="author"
    )
    assigned_tickets = db.relationship(
        "Ticket",
        foreign_keys="Ticket.technician_id",
        back_populates="technician",
    )

    # --- Logique métier ------------------------------------------------------

    def add_role(self, role: Role):
        """Ajoute un rôle (sans doublon)."""
        if role.name in self.role_names():
            return
        user_role = UserRole()
        user_role.rel_role = role
        user_role.rel_user = self
        self.roles.append(user_role)

    def remove_role(self, role: Role):
        """Supprime un rôle à un utilisateur."""
        for user_role in self.roles:
            if user_role.role_id == role.role_id:
                self.roles.remove(user_role)
                return

    def get_roles(self) -> list[Role]:
        return [user_role.rel_role for user_role in self.roles]

    def is_admin(self) -> bool:
        return "ADMIN" in self.role_names()

    def has_role(self, rolename: str) -> bool:
        return rolename in self.role_names()

    # --- Utils ------------------------------------------------------------------

    def role_names(self) -> list[str]:
        return [user_role.rel_role.name for user_role in self.roles]

    def __repr__(self):
        return f"<User {self.name}>"
