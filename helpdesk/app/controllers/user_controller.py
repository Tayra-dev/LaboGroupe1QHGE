from flask import render_template, redirect

from app import app
from app.framework.decorators.inject import inject
from app.forms.users.user_register_form import UserRegisterForm


@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("users/register.html", form=form)
