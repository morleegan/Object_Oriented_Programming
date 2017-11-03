from flask import Blueprint

ticket = Blueprint('ticket', __name__)


@ticket.route('/<int:tid>', methods=['GET', 'DELETE'])
def req_view_t(tid):
    return "ticket " + str(tid)


@ticket.route('/', methods=['GET', 'POST'])
def req_view_all_t():
    return "ticket index"


@ticket.route('/donations', methods=['GET', 'POST'])
def req_ticket_donations():
    return "donations"

