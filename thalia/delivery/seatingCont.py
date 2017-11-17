from flask import Blueprint, request, jsonify
from thalia.emulator import TheaterEmulator

seating = Blueprint('seating', __name__)
theater_emu = TheaterEmulator()


@seating.route('/seating', methods=['GET'])
def req_view_all():
    # TODO: find seats specific (not in the api)
    if sorted(['show', 'section', 'count']) == sorted(request.args.keys()):
        wid = request.args['show']
        sid = request.args['section']
        count = request.args['count']
        # return jsonify(section_emu.make_seats_request(wid, sid, count))
    return jsonify(theater_emu.make_json())


@seating.route('/seating/<wid>', methods=['GET'])
def req_view(wid):
    return jsonify(theater_emu.make_section_by_id(sid=wid))