from flask import jsonify
from app.models.ticket import Ticket
from flask import render_template
from app import app, csrf
from app.forms.tickets.ticket_form import TicketForm
from app.services.ticket_service import TicketService
from app.services.category_service import CategoryService
from app.services.priority_service import PriorityService

# Temporary import
from app.models.equipment import Equipment

@app.route("/tickets/create", methods=["GET", "POST"])
# ! For Direct Url API Testing (PostMan)
# @csrf.exempt
def create_ticket():
    # ! For Direct Url API Testing (PostMan)
    # form = TicketForm(meta={"csrf": False})
    form = TicketForm()

    # Load options from db for categories, priorities
    # and equipment into forms (temporary bypass for equipments)
    category_service = CategoryService()
    priority_service = PriorityService()

    # Note for later:
    # WTForms except to recieve (value stored in db, value displayed in html for user)
    # when it comes to select fields.
    form.category_id.choices = [
        (category.category_id, category.category_name) for category in category_service.find_all()
    ]
    form.priority_id.choices = [
        (priority.priority_id, priority.priority_name) for priority in priority_service.find_all()
    ]
    # Line to change with EquipmentService.find_all() once available 
    form.equipment_id.choices = [
        (equipment.equipment_id, equipment.name) for equipment in Equipment.query.all()
    ]


    if form.validate_on_submit():
        TicketService().insert(form)
        return "SUCCESS", 201
    # ! For Direct Url API Testing (PostMan)
    # return f"VALIDATION ERROR: {form.errors}", 400 
    return render_template("tickets/create.html", form=form)

@app.route("/tickets", methods=["GET"])
# ! For Direct Url API Testing (PostMan)
# @csrf.exempt
def display_all_tickets():
    tickets = TicketService().find_all()
    return render_template("tickets/display_all.html", tickets=tickets)  