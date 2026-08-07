from flask import render_template

from app import app
from app.framework.decorators.inject import inject
from app.forms.users.user_register_form import UserRegisterForm


@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        print(form)
    return render_template("users/register.html", form=form)
