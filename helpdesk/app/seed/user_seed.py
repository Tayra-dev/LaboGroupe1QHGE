from argon2 import PasswordHasher

from app import app, db
from app.framework.seed import Seedable
from app.models.user import User
from app.models.role import Role
from app.seed import USERS


class UserSeed(Seedable):
    order: 20

    def seed(self):
        for (
            name,
            email,
            password,
            firstname,
            lastname,
            roles,
        ) in USERS:
            if User.query.filter_by(name=name).first() is not None:
                app.logger.debug(f"Seed user {name}: déjà présent")
                continue

            user = User(
                name=name,
                email=email,
                password=PasswordHasher.hash(password),
                firstname=firstname,
                lastname=lastname,
            )

            db.session.add(user)

            for name in roles:
                role = Role.query.filter_by(name=name).first()
                user.add_role(role)

            app.logger.debug(f"Seed user {name}")
        db.session.commit()
