from flask import Blueprint, request, jsonify
from thalia.emulator import ShowEmulator

show_main = Blueprint('show_main', __name__)
show_emu = ShowEmulator()


@show_main.route('/', methods=['GET', 'POST'])
def req_view_all():
    if request.method == 'POST':
        content = request.get_json()
        showinfo = content['show_info']
        seating = content['seating_info']
        r_json = show_emu.make_object(showinfo=showinfo, seating=seating)
        return jsonify(r_json)
    else:
        return jsonify(show_emu.make_json())


@show_main.route('/<wid>', methods=['GET', 'PUT'])
def req_view(wid):
    if request.method == 'PUT':
        content = request.get_json()
        s = show_emu.update_object(wid=wid, show_info=content['show_info'], seating=content['seating_info'])
        return jsonify(s)
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
