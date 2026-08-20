from flask import redirect, render_template

from app import app
from app.framework.decorators.inject import inject
from app.framework.decorators.auth_required import auth_required
from app.forms.teams.team_form import TeamForm
from app.services.user_service import UserService


@app.route("/teams/add", methods=["GET", "POST"])
@auth_required()
@inject
def create_team(user_service: UserService):
    form = TeamForm()
    users = user_service.find_all()
    users_by_id = {user.user_id: user for user in users}

    form.members.choices = [
        (user.user_id, f"{user.firstname} {user.lastname}") for user in users
    ]

    members_data = [(subfield, users_by_id[subfield.data]) for subfield in form.members]

    if form.validate_on_submit():
        print("success")
        # TeamService().insert(form)
    return render_template(
        "teams/add_or_update.html", form=form, team=None, members_data=members_data
    )
