from flask import Blueprint

ticket = Blueprint('ticket', __name__)


@ticket.route('/<tid>', methods=['GET'])
def req_view_t(tid):
    return "ticket " + str(tid)


@ticket.route('/', methods=['POST'])
def req_view_all_t():
    return "ticket index"


@ticket.route('/donations', methods=['GET', 'POST'])
def req_ticket_donations():
    return "donations"

