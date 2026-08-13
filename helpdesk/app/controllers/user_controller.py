from flask import redirect, render_template

from app import app
from app.framework.decorators.inject import inject
from app.forms.users.user_register_form import UserRegisterForm
from app.forms.users.user_login_form import UserLoginForm
from app.services.user_service import UserService
from app.framework.service.abstract_auth_service import AbstractAuthService


@app.route("/register", methods=["GET", "POST"])
@inject
def register(user_service: UserService, auth_service: AbstractAuthService):
    if auth_service.is_authenticated():
        return redirect("/dashboard")
    form = UserRegisterForm()
    if form.validate_on_submit():
        user = user_service.insert(form)
        if user is not None:
            auth_service.login(user)
            return redirect("/dashboard")
    return render_template("users/register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
@inject
def login(user_service: UserService, auth_service: AbstractAuthService):
    if auth_service.is_authenticated():
        return redirect("/dashboard")
    form = UserLoginForm()
    error = None
    if form.validate_on_submit():
        user = user_service.login(form)
        if user is not None:
            auth_service.login(user)
            return redirect("/dashboard")
        else:
            error = "Identifiant ou mot de passe incorrect"
    return render_template("users/login.html", form=form, error=error)


@app.route("/logout", methods=["GET"])
@inject
def logout(auth_service: AbstractAuthService):
    auth_service.logout()
    return redirect("/")


@app.route("/dashboard", methods=["GET", "POST"])
@inject
def goToDashboard(auth_service: AbstractAuthService):
    if not auth_service.is_authenticated():
        return redirect("/")
    return render_template("dashboard/dashboard.html")
