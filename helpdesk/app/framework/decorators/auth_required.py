from flask import redirect, request, url_for, abort, flash
from functools import wraps
from app import app


def auth_required(role_name=None, or_is_current_user=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            auth_service = app.injector["AbstractAuthService"]
            current_user = auth_service.get_current_user()

            if current_user is None:
                flash("Vous devez être connecté pour accéder à cette page.", "warning")
                return redirect(url_for("login", next=request.path))
            if current_user.is_admin():
                return func(*args, **kwargs)
            if role_name is not None and current_user.has_role(role_name):
                return func(*args, **kwargs)
            if or_is_current_user and current_user.user_id == kwargs.get("user_id"):
                return func(*args, **kwargs)
            if not role_name and not or_is_current_user:
                return func(*args, **kwargs)
            abort(403)

        return wrapper

    return decorator
