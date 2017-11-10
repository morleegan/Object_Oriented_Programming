from flask import Blueprint, request

order = Blueprint('order', __name__)


@order.route('/orders/', methods=['GET', 'POST'])
def req_view_all():
    if request.method == 'POST':
        pass
    else:
        pass


@order.route('/orders/<wid>', methods=['GET'])
def req_view(wid):
    return "sid " + str(wid)


@order.route('/orders', methods=['GET'])
def req_order_by_dates():
    # ?start_date = YYYYMMDD & end_date = YYYYMMDD
    start = request.args.get('start_date', type=str)    # TODO: will have to parse
    end = request.args.get('end_date', type=str)
    return "start: " + start


