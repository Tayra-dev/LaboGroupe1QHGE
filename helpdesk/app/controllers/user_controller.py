from flask import redirect, render_template

from app import app
from app.framework.decorators.inject import inject
from app.forms.users.user_register_form import UserRegisterForm
from app.forms.users.user_login_form import UserLoginForm
from app.services.user_service import UserService
from app.framework.service.abstract_auth_service import AbstractAuthService


@app.route("/register", methods=["GET", "POST"])
@inject
def register(user_service: UserService):
    form = UserRegisterForm()
    if form.validate_on_submit():
        user_service.insert(form)
        # TODO: return redirect("/success") or log user automatically
    return render_template("users/register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
@inject
def login(user_service: UserService, auth_service: AbstractAuthService):
    form = UserLoginForm()
    error = None
    if form.validate_on_submit():
        user = user_service.login(form)
        if user is not None:
            auth_service.login(user)
            # TODO: redirect(...)
        else:
            error = "Identifiant ou mot de passe incorrect"
    return render_template("users/login.html", form=form, error=error)
