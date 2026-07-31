from app.dtos.abstract_dto import AbstractDTO
from app.dtos.role_dto import RoleDTO
from app.models.user import User


class UserDTO(AbstractDTO):
    def __init__(self):
        self.user_id = None
        self.name = None
        self.email = None
        self.firstname = None
        self.lastname = None
        self.roles = []

    @staticmethod
    def build_from_entity(user: User) -> "UserDTO":
        user_dto = UserDTO()
        user_dto.user_id = user.user_id
        user_dto.name = user.name
        user_dto.email = user.email
        user_dto.firstname = user.firstname
        user_dto.lastname = user.lastname
        user_dto.roles = [RoleDTO.build_from_entity(ur.role) for ur in user.roles]
        return user_dto

    def get_json_parsable(self):
        data = dict(self.__dict__)
        data["roles"] = [role.get_json_parsable() for role in self.roles]
        return data
