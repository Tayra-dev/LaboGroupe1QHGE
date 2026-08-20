from app import app
from flask import render_template, redirect, url_for, flash
from app.services.site_service import SiteService
from app.framework.decorators.inject import inject

@app.get('/sites')
@inject
def site_list(site_service: SiteService):
    return render_template('sites/list.html', sites=site_service.find_all())

