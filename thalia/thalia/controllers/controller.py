from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def req_view():
    return "index"


@main.route('/<int:wid>', methods=['GET', 'PUT', 'DELETE'])
def req_view_all(wid):
    return "sid " + str(wid)







