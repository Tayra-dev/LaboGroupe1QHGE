from flask import redirect, url_for, abort
from functools import wraps
from app import app


def auth_required(role_name=None, or_is_current_user=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            auth_service = app.injector["AbstractAuthService"]
            current_user = auth_service.get_current_user()
            current_user_is_authorized = True
            current_user_is_admin = True

            if current_user is None:
                return redirect(url_for("login"))
            if role_name is not None:
                user_role_names = [role.name for role in current_user.roles]
                if role_name not in user_role_names:
                    current_user_is_admin = False
            if or_is_current_user:
                current_user_is_authorized = current_user.user_id == kwargs.get("user_id")
            if not current_user_is_admin and not current_user_is_authorized:
                abort(403)
            return func(*args, **kwargs)
        return wrapper
    return decorator
