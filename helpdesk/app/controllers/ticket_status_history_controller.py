from app import app
from flask import flash, redirect, url_for, render_template
from app.framework.decorators.inject import inject
from app.services.ticket_status_history_service import TicketStatusHistoryService
from app.framework.service.abstract_auth_service import AbstractAuthService

@app.route('/tickets/<ticket_id>/status-history', methods=['GET'])
@inject
def get_history_by_ticket(
    ticket_id: int,
    ticket_status_history_service: TicketStatusHistoryService,
    auth_service: AbstractAuthService
):
    if not auth_service.is_authenticated():
        flash("Vous devez être connecté.")
        return redirect(url_for("login"))

    status_histories = ticket_status_history_service.find_all_by(ticket_id=ticket_id)

    if not status_histories:
        app.logger.error(f"Error | get history by ticket impossible")
        flash(f"Impossible de renvoyer l'historique du ticket {ticket_id}")
        # return redirect(url_for("display_ticket", ticket_id=ticket_id))

    return render_template(
        "ticketstatushistories/status-history.html",
        status_histories= status_histories,
        ticket_id= ticket_id
    )



@app.route('/tickets/status-histories', methods=['GET'])
@inject
def get_all_histories():
    pass
