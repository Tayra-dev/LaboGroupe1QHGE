from app.framework.service.abstract_auth_service import AbstractAuthService
from app.framework.decorators.injectable import injectable
from app.framework.injector import Scope

from app.dtos.user_dto import UserDTO


@injectable(base=AbstractAuthService, scope=Scope.SCOPED)
class AuthService(AbstractAuthService):
    def get_current_user(self):
        pass

    def login(self, user: UserDTO) -> None:
        pass

    def logout(self):
        pass

    def is_authenticated(self) -> bool:
        pass
