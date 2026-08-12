from flask import redirect, render_template

from app import app
from app.framework.decorators.inject import inject
from app.forms.users.user_register_form import UserRegisterForm
from app.forms.users.user_login_form import UserLoginForm
from app.services.user_service import UserService


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
def login(user_service: UserService):
    form = UserLoginForm()
    if form.validate_on_submit():
        # TODO: call auth service
        pass
    return render_template("users/login.html", form=form)