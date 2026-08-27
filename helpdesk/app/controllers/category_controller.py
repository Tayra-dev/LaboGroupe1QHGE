from app.framework.decorators.inject import inject
from flask import render_template
from app import app, csrf
from app.forms.categories.category_form import CategoryForm
from app.services.category_service import CategoryService

@inject
@app.route("/categories/create", methods=["GET", "POST"])
def create_category(
    category_service: CategoryService
):
    form = CategoryForm()
    if form.validate_on_submit():
        category_service.insert(form)
        return "SUCCESS", 201
    return render_template("categories/create.html", form=form)