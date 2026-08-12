from flask import render_template

from app import app
from app.framework.decorators.inject import inject

@app.get('/')
@inject
def index():
    return render_template("/home/home.html")