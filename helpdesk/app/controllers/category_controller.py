from flask import redirect, render_template

from app import app
from app.forms.categories.category_form import CategoryForm
from app.services.category_service import CategoryService

@app.route("/categories/create", methods=["GET", "POST"])
def create_category():
    form = CategoryForm()
    if form.validate_on_submit():
        CategoryService().insert(form)
    return render_template("categories/create.html", form=form)


