from app.framework.decorators.inject import inject
from flask import render_template
from app import app, csrf
from app.forms.priorities.priority_form import PriorityForm
from app.services.priority_service import PriorityService

@inject
@app.route("/priorities/create", methods=["GET", "POST"])
# ! For Direct Url API Testing (PostMan)
# @csrf.exempt

def create_priority(
    priority_service: PriorityService
):
    # ! For Direct Url API Testing (PostMan)
    # form = PriorityForm(meta={"csrf": False})
    form = PriorityForm()
    if form.validate_on_submit():
        priority_service.insert(form)
        return "SUCCESS", 201
    return render_template("priorities/create.html", form=form)
    # ! For Direct Url API Testing (PostMan)
    # return f"VALIDATION ERROR: {form.errors}", 400 