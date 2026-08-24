from flask import redirect, render_template, flash

from app import app
from app.framework.decorators.inject import inject
from app.framework.decorators.auth_required import auth_required
from app.forms.teams.team_form import TeamCreationForm
from app.services.user_service import UserService
from app.services.team_service import TeamService


@app.route("/teams")
@auth_required(role_name="ADMIN")
@inject
def team_list(team_service: TeamService):
    pass


@app.route("/teams/add", methods=["GET", "POST"])
@app.route("/teams/<int:team_id>/edit", methods=["GET", "POST"])
@auth_required(role_name="ADMIN")
@inject
def create_team(team_service: TeamService, user_service: UserService):
    form = TeamCreationForm()
    users = [
        user
        for user in user_service.find_all()
        if (user.has_role("TECHNICIEN") and user.team_id is None)
    ]
    users_by_id = {user.user_id: user for user in users}

    form.members.choices = [
        (user.user_id, f"{user.firstname} {user.lastname}") for user in users
    ]

    members_data = [(subfield, users_by_id[subfield.data]) for subfield in form.members]

    if form.validate_on_submit():
        app.logger.info(f"form sent successfully: ${form.members.data}")
        team = team_service.insert(form, user_service)
        if team is not None:
            flash("L'équipe {team.name} a été créée correctement.", "success")
    return render_template(
        "teams/add_or_update.html", form=form, team=None, members_data=members_data
    )
