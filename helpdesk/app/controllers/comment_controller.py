from app import app
from flask import flash, redirect, url_for, render_template

# from app.framework.decorators.auth_required import auth_required
from app.services.comment_service import CommentService
from app.services.auth_service import AuthService
from app.forms.comment_form import CommentForm

@app.route('/tickets/<ticket_id>/comments', methods=['GET', 'POST'])
# + Ajouter un décorateur qui vérifie que l'auteur du commentaire est loggé
def comment_create(
    ticket_id: int,
    comment_service: CommentService,
    auth_service: AuthService 
):
    """Création d'un commentaire sur un ticket"""

    form = CommentForm()

    if form.validate_on_submit():

        current_user = auth_service.get_current_user() #controller le nom de la fonction dans auth_service

        data = {
            "form": form,
            "author_id": current_user.user_id,
            "ticket_id": ticket_id
        }

        comment = comment_service.insert(data)

        if comment is None:
            app.logger.error(f"Error | comment create impossible")
            flash("Impossible de créer le commentaire.")
        
        else:
            flash("Commentaire ajouté avec succès.")
            # return redirect(url_for("ticket_detail", ticket_id=ticket_id))

    return render_template(
        "comments/create.html",
        form=form,
        ticket_id=ticket_id
    )
