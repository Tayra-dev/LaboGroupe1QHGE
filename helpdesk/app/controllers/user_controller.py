from flask import redirect, render_template

from app import app
from app.forms.users.user_register_form import UserRegisterForm
from app.services.user_service import UserService


@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        UserService().insert(form)
        #return redirect("/success")
    return render_template("users/register.html", form=form)
