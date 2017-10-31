from flask import Blueprint

show_main = Blueprint('show_main', __name__)


@show_main.route('/<int:wid>/sections/<int:sid>', methods=['GET'])
def req_show_section(wid, sid):
    return "show: " + str(wid) + " section " + str(sid)


@show_main.route('/<int:wid>/donations/<int:did>', methods=['GET'])
def req_show_donation(wid, did):
    return "show: " + str(wid) + " donation: " + str(did)


@show_main.route('/<int:wid>/donations', methods=['POST'])
def req_all_donations(wid):
    pass
