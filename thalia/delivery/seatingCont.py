from flask import Blueprint, request

seating = Blueprint('seating', __name__)


@seating.route('/seating/', methods=['GET', 'POST'])
def req_view_all():
    if request.method == 'POST':
        pass
    else:
        pass


@seating.route('/seating/<int:wid>', methods=['GET', 'PUT', 'DELETE'])
def req_view(wid):
    if request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return "sid " + str(wid)


@seating.route('/seating', methods=['GET'])
def req_seats_auto():
    # ?show=<int:wid>&section=<int:sid>&count=<int:count>
    wid = request.args.get('show', type=int)
    sid = request.args.get('section', type=int)
    count = request.args.get('count', type=int)
    return "wid: " + str(wid) + " sid: " + str(sid) + " count: " + str(count)


@seating.route('/seating', methods=['GET'])
def req_specific_seats():
    # ?show=<int:wid>&section=<int:sid>&seats=[<cid>]
    wid = request.args.get('wid', type=int)
    sid = request.args.get('sid', type=int)
    seats = request.args.get('seats', type=list)   # list of cids
    return "this will call get specific seats"

