from app import app
from flask import render_template, redirect, url_for, flash
from app.services.site_service import SiteService
from app.forms.sites.site_form import SiteForm
from app.framework.decorators.inject import inject

@app.get('/sites')
@inject
def site_list(site_service: SiteService):
    return render_template('sites/list.html', sites=site_service.find_all())

@app.route('/sites/create', methods=['GET', 'POST'])
@inject
def site_create(site_service: SiteService):
    form = SiteForm()

    if form.validate_on_submit():
        site = site_service.insert(form)

        if site is None:
            flash("Impossible de créer le site.", "danger")
        else:
            flash(f"Site « {site.name} » créé.", "success")
            return redirect(url_for('site_list'))

    return render_template('sites/add_or_update.html', form=form, site=None)

@app.route('/sites/<int:site_id>/edit', methods=['GET', 'POST'])
@inject
def site_update(site_id: int, site_service: SiteService):
    site = site_service.find_one(site_id)

    if site is None:
        flash("Site introuvable.", "warning")
        return redirect(url_for('site_list'))

    form = SiteForm()

    if form.validate_on_submit():
        updated = site_service.update(site_id, form)

        if updated is None:
            flash("Modification impossible.", "danger")
        else:
            flash("Site mis à jour.", "success")
            return redirect(url_for('site_details', site_id=site_id))
        
    return render_template('sites/add_or_update.html', form=form, site=site)

@app.get('/sites/<int:site_id>')
@inject
def site_details(site_id: int, site_service: SiteService):
    site = site_service.find_one(site_id)

    if site is None:
        flash("Site introuvable.", "warning")
        return redirect(url_for('site_list'))

    return render_template('sites/details.html', site=site)

@app.post('/sites/<int:site_id>')
@inject
def site_delete(site_id: int, site_service: SiteService):
    if site_service.delete(site_id) is None:
        flash("Suppression impossible.", "danger")
    else:
        flash("Site supprimé.", "success")

    return redirect(url_for('site_list'))
