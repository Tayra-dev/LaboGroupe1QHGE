from app import app
from app.framework.decorators.inject import inject
from app.framework.decorators.auth_required import auth_required
from app.services.user_service import UserService

@app.route("/api/users")
@auth_required(role_name="ADMIN")
@inject
def get_all_users(user_service: UserService):
    users = user_service.find_all()
    app.logger.debug("test")
    app.logger.debug(users.get_json_parsable())
