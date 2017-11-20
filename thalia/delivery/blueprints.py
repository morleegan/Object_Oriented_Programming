from flask import Blueprint, request, jsonify
from thalia.emulator import ShowEmulator, TheaterEmulator, OrderEmulator

show_main = Blueprint('show_main', __name__)
seating = Blueprint('seating', __name__)
ticket = Blueprint('ticket', __name__)
search = Blueprint('search', __name__)
report = Blueprint('report', __name__)
order = Blueprint('order', __name__)

show_emu = ShowEmulator()
theater_emu = TheaterEmulator()
order_emu = OrderEmulator()


""" Show Controller """


@show_main.route('/', methods=['GET', 'POST'])
def req_view_all():
    if request.method == 'POST':
        content = request.get_json()
        return jsonify(show_emu.make_object(showinfo=content['show_info'], seating=content['seating_info']))
    else:
        return jsonify(show_emu.make_json())


@show_main.route('/<wid>', methods=['GET', 'PUT'])
def req_view(wid):
    if request.method == 'PUT':
        content = request.get_json()
        return jsonify(show_emu.update_object(wid=wid, show_info=content['show_info'], seating=content['seating_info']))
    else:
        return jsonify(show_emu.make_json_by_id(wid))


@show_main.route('/<wid>/sections', methods=['GET'])
def req_show_section(wid):
    return jsonify(show_emu.make_json_by_sections(wid))


@show_main.route('/<wid>/sections/<sid>', methods=['GET'])
def req_show_section_by_sid(wid, sid):
    return jsonify(show_emu.make_json_by_section_sid(wid=wid, sid=sid))


@show_main.route('/<int:wid>/donations/<int:did>', methods=['GET'])
def req_show_donation(wid, did):
    return "show: " + str(wid) + " donation: " + str(did)


@show_main.route('/<int:wid>/donations', methods=['POST'])
def req_all_donations(wid):
    pass


""" SEATING CONTROLLER """


@seating.route('/seating', methods=['GET'])
def req_view_all():
    if sorted(['show', 'section', 'count']) == sorted(request.args.keys()):
        wid = request.args['show']
        sid = request.args['section']
        count = request.args['count']
        return jsonify(show_emu.make_seats_request(wid=wid, sid=sid, count=count))
    return jsonify(theater_emu.make_json())


@seating.route('/seating/<sid>', methods=['GET'])
def req_view(sid):
    return jsonify(theater_emu.make_section_by_id(sid=sid))


""" Ticket Controller """


@ticket.route('/<tid>', methods=['GET'])
def req_view_t(tid):
    return "ticket " + str(tid)


@ticket.route('/', methods=['POST'])
def req_view_all_t():
    return "ticket index"


@ticket.route('/donations', methods=['GET', 'POST'])
def req_ticket_donations():
    return "donations"


""" search controller """


@search.route('/search', methods=['GET'])
def req_report():
    # search?topic=topicword&key=keyword
    topic = request.args.get('topicword', type=str)
    key = request.args.get('keyword', type=str)
    return "keyword and topic: " + key + " " + topic


""" Report Controller """


@report.route('/', methods=['GET'])
def req_view():
    return "report index"


@report.route('/<mrid>', methods=['GET'])
def req_report(mrid):
    # ?show={wid} | ?start_date=YYYYMMDD&end_date=YYYYMMDD
    wid = request.args.get('show', type=int)
    start = request.args.get('start_date', type=str)    # TODO: will have to parse
    end = request.args.get('end_date', type=str)
    return "start: " + start


""" Order Controller """


@order.route('/orders/', methods=['GET', 'POST'])
def req_view_all():
    if request.method == 'POST':
        pass
    else:
        all_returned = list()
        # TODO: get all orders
        orders = list()
        for o in orders:
            all_returned.append(OrderEmulator.make_json(o))
        return jsonify(all_returned)


@order.route('/orders/<oid>', methods=['GET'])
def req_view(oid):
    # TODO: solve the finding of order when you have oid, incorrect call
    oid_order = None
    return OrderEmulator.make_json_w_oid(oid_order)


@order.route('/orders', methods=['GET'])
def req_order_by_dates():
    # ?start_date = YYYYMMDD & end_date = YYYYMMDD
    start = request.args.get('start_date', type=str)    # TODO: will have to parse
    end = request.args.get('end_date', type=str)
    return "start: " + start


