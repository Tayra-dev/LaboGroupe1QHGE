from sqlalchemy.exc import SQLAlchemyError
from argon2 import PasswordHasher

from app import app, db
from app.framework.service.abstract_service import AbstractService
from app.dtos.user_dto import UserDTO
from app.forms.users.user_register_form import UserRegisterForm
from app.mappers.user_mapper import UserMapper
from app.models.role import Role
from app.models.user import User


class UserService(AbstractService):
    def __init__(self):
        self.__hasher = PasswordHasher()

    def find_all(self):
        pass

    def find_one(self, entity_id: int):
        pass

    def find_one_by(self, **kwargs):
        pass

    def insert(self, form: UserRegisterForm) -> UserDTO | None:
        try:
            user = User()
            UserMapper.form_to_entity(form, user)

            user.password = self.__hasher.hash(user.password)

            role = Role.query.filter_by(name="USER").first()
            if role is not None:
                user.add_role(role)

            db.session.add(user)
            db.session.commit()

        except SQLAlchemyError as e:
            db.session.rollback()
            app.logger.error(f"Erreur lors de la création de l'utilisateur: {e}")
            return None
        else:
            return UserMapper.entity_to_dto(user)

    def update(self, entity_id: int, data):
        pass

    def delete(self, entity_id: int):
        pass
