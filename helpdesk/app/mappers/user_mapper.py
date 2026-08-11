from app.dtos.user_dto import UserDTO
from app.forms.users.user_register_form import UserRegisterForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.user import User


class UserMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(user: User) -> UserDTO:
        return UserDTO.build_from_entity(user)

    @staticmethod
    def form_to_entity(form, user: User) -> User:
        if isinstance(form, UserRegisterForm):
            user.name = form.name.data
            user.email = form.email.data
            user.password = form.password.data
            user.firstname = form.firstname.data
            user.lastname = form.lastname.data
        return user
