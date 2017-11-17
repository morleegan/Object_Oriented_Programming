from flask import Blueprint, request, jsonify
from thalia.emulator import OrderEmulator
from thalia.order import Orders

order = Blueprint('order', __name__)


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
    oid_order = Orders(oid)
    return OrderEmulator.make_json_w_oid(oid_order)


@order.route('/orders', methods=['GET'])
def req_order_by_dates():
    # ?start_date = YYYYMMDD & end_date = YYYYMMDD
    start = request.args.get('start_date', type=str)    # TODO: will have to parse
    end = request.args.get('end_date', type=str)
    return "start: " + start


