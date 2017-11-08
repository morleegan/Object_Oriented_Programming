from flask import Blueprint, request
from thalia.utilities.response import call_parser

show_main = Blueprint('show_main', __name__)


@show_main.route('/', methods=['GET', 'POST'])
def req_view_all():
    if request.method == 'POST':
        content = request.json
        obj = call_parser(content)
    else:
        pass


@show_main.route('/<int:wid>', methods=['GET', 'PUT', 'DELETE'])
def req_view(wid):
    if request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return "sid " + str(wid)


@show_main.route('/<int:wid>/sections/<int:sid>', methods=['GET'])
def req_show_section(wid, sid):
    return "show: " + str(wid) + " section " + str(sid)


@show_main.route('/<int:wid>/donations/<int:did>', methods=['GET'])
def req_show_donation(wid, did):
    return "show: " + str(wid) + " donation: " + str(did)


@show_main.route('/<int:wid>/donations', methods=['POST'])
def req_all_donations(wid):
    pass
