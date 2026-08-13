from flask import render_template
from app import app, csrf
from app.forms.priorities.priority_form import PriorityForm
from app.services.priority_service import PriorityService

@app.route("/priorities/create", methods=["GET", "POST"])
@csrf.exempt
def create_priority():
    # ! For Direct Url API Testing (PostMan)
    form = PriorityForm(meta={"csrf": False})
    # form = PriorityForm()
    if form.validate_on_submit():
        PriorityService().insert(form)
        return "SUCCESS", 201
    # return render_template("priorities/create.html", form=form)
    # ! For Direct Url API Testing (PostMan)
    return f"VALIDATION ERROR: {form.errors}", 400 