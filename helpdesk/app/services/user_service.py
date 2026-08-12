from argon2 import PasswordHasher
from sqlalchemy.exc import SQLAlchemyError

from app import app, db
from app.framework.decorators.injectable import injectable
from app.framework.injector import Scope
from app.framework.service.abstract_service import AbstractService
from app.dtos.user_dto import UserDTO
from app.forms.users.user_register_form import UserRegisterForm
from app.models.role import Role
from app.models.user import User
from app.mappers.user_mapper import UserMapper


@injectable(scope=Scope.SCOPED)
class UserService(AbstractService):
    def __init__(self):
        self.__hasher = PasswordHasher()

    def find_all(self) -> list[UserDTO]:
        try:
            users = User.query.filter_by(active=True).order_by(User.user_id).all()
        except SQLAlchemyError as e:
            db.session.rollback()
            app.logger.error(
                f"Erreur lors de la sélection de tous les utilisateurs: {e}"
            )
            return []
        else:
            return [UserMapper.entity_to_dto(user) for user in users]

    def find_one_entity(self, entity_id: int) -> User | None:
        try:
            return db.session.get(User, entity_id)
        except SQLAlchemyError as e:
            db.session.rollback()
            app.logger.error(
                f"Erreur lors de la récupération de l'utilisateur, id {entity_id}: {e}"
            )
            return None

    def find_one(self, entity_id: int) -> UserDTO | None:
        try:
            user = db.session.get(User, entity_id)
            return UserMapper.entity_to_dto(user) if user is not None else None
        except SQLAlchemyError as e:
            db.session.rollback()
            app.logger.error(
                f"Erreur lors de la récupération de l'utilisateur (DTO), id {entity_id}: {e}"
            )
            return None

    def find_one_by(self, **kwargs) -> UserDTO | None:
        try:
            user = User.query.filter_by(**kwargs).first()
            return UserMapper.entity_to_dto(user) if user is not None else None
        except SQLAlchemyError as e:
            db.session.rollback()
            app.logger.error(
                f"Erreur lors de la récupération de l'utilisateur (DTO) avec {[f'{k} = {v}' for k, v in kwargs.items()]} : {e}"
            )
            return None

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

    def update(self, entity_id: int, data) -> UserDTO | None:
        try:
            user = self.find_one_entity(entity_id)
            if user is None:
                return None
            UserMapper.form_to_entity(data, user)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            app.logger.error(
                f"Erreur lors de la mise à jour de l'utilisateur {entity_id}: {e}"
            )
            return None
        else:
            return UserMapper.entity_to_dto(user)

    def delete(self, entity_id: int) -> int | None:
        try:
            user = self.find_one_entity(entity_id)
            if user is None:
                return None
            user.soft_delete()
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            app.logger.error(
                f"Erreur lors de la suppression de l'utilisateur {entity_id}: {e}"
            )
            return None
        else:
            return entity_id
