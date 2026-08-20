from app import app
from flask import flash, redirect, url_for, render_template
from app.framework.decorators.inject import inject
from app.services.attachment_service import AttachmentService
from app.forms.attachment_form import AttachmentForm
from app.framework.service.abstract_auth_service import AbstractAuthService


@app.route('/tickets/<ticket_id>/attachments/create', methods=['GET', 'POST'])
@inject
def attachment_create(
    attachment_service: AttachmentService,
    auth_service: AbstractAuthService,
    ticket_id: int
):
    """Création d'une pièce jointe sur un ticket"""

    if not auth_service.is_authenticated():
        flash("Vous devez être connecté.", "error")
        return redirect(url_for("login"))

    form = AttachmentForm()

    if form.validate_on_submit():
        data = {
            "form": form,
            "author_id": auth_service.get_current_user().user_id,
            "ticket_id": ticket_id
        }

        result = attachment_service.insert(data)

        if result is None:
            app.logger.error(f"Error | attachment create impossible")
            flash("Impossible d'ajouter la pièce jointe", "error")

        else:
            flash("La pièce jointe a été ajoutée avec succès", "success")
            return redirect(url_for("index"))

    return render_template(
        "attachments/create.html",
        form= form,
        ticket_id= ticket_id
    )
