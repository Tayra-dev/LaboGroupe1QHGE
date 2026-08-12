from app.framework.service.abstract_auth_service import AbstractAuthService
from app.framework.decorators.injectable import injectable
from app.framework.injector import Scope

@injectable(base=AbstractAuthService, scope=Scope.SCOPED)
class AuthService(AbstractAuthService):
    pass
