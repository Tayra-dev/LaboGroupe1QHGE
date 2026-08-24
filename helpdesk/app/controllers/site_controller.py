from app import app
from flask import render_template, redirect, url_for, flash, request
from app.services.site_service import SiteService
from app.services.user_service import UserService
from app.services.equipment_service import EquipmentService
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
            flash("Impossible de créer le site.", "error")
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
            flash("Modification impossible.", "error")
        else:
            flash("Site mis à jour.", "success")
            return redirect(url_for('site_details', site_id=site_id))
        
    return render_template('sites/add_or_update.html', form=form, site=site)

@app.get('/sites/<int:site_id>')
@inject
def site_details(site_id: int, site_service: SiteService, user_service: UserService, equipment_service: EquipmentService):
    site = site_service.find_one(site_id)

    if site is None:
        flash("Site introuvable.", "warning")
        return redirect(url_for('site_list'))

    return render_template('sites/details.html', site=site, users=user_service.find_all(), equipments=equipment_service.find_all())

@app.post('/sites/<int:site_id>')
@inject
def site_delete(site_id: int, site_service: SiteService):
    if site_service.delete(site_id) is None:
        flash("Suppression impossible.", "error")
    else:
        flash("Site supprimé.", "success")

    return redirect(url_for('site_list'))

@app.post('/sites/<int:site_id>/add-users')
@inject
def site_assign_user(site_id: int, site_service: SiteService, user_service: UserService):
    user_id = request.form.get('user_id', type=int)

    if user_id is None:
        flash("Utilisateur invalide", "error")
        return redirect(url_for('site_details', site_id=site_id))

    user = user_service.find_one_entity(user_id)

    if user is None:
        flash("Utilisateur invalide", "error")
        return redirect(url_for('site_details', site_id=site_id))

    if site_service.assign_user(user, site_id) is None:
        flash("Assignement impossible.", "error")
    else:
        flash("Utilisateur assigné.", "success")

    return redirect(url_for('site_details', site_id=site_id) + '#users')

@app.post('/sites/<int:site_id>/remove-users')
@inject
def site_remove_user(site_id: int, site_service: SiteService, user_service: UserService):
    user_id = request.form.get('user_id', type=int)

    if user_id is None:
        flash("Utilisateur invalide", "error")
        return redirect(url_for('site_details', site_id=site_id))

    user = user_service.find_one_entity(user_id)

    if user is None:
        flash("Utilisateur invalide", "error")
        return redirect(url_for('site_details', site_id=site_id))

    if site_service.remove_user(user, site_id) is None:
        flash("Impossible de retirer l'utilisateur.", "error")
    else:
        flash("Utilisateur retiré.", "success")
    
    return redirect(url_for('site_details', site_id=site_id) + '#users')

@app.post('/sites/<int:site_id>/add-equipment')
@inject
def site_assign_equipment(site_id: int, site_service: SiteService, equipment_service: EquipmentService):
    equipment_id = request.form.get('equipment_id', type=int)

    if equipment_id is None:
        flash("Equipement invalide", "error")
        return redirect(url_for('site_details', site_id=site_id))

    equipment = equipment_service.find_one_entity(equipment_id)

    if equipment is None:
        flash("Equipement invalide", "error")
        return redirect(url_for('site_details', site_id=site_id))

    if site_service.assign_equipment(equipment, site_id) is None:
        flash("Assignement impossible.", "error")
    else:
        flash("Equipement assigné.", "success")

    return redirect(url_for('site_details', site_id=site_id) + '#equipment')