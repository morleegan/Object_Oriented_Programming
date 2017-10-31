from flask import Flask, url_for, request, jsonify

from thalia.static.get import get_show, get_all_shows
"""API calls for Thalia"""

app = Flask(__name__)


@app.route('/thalia')
def index():
    return 'index_page'


@app.route('/thalia/shows/<wid>', methods=['GET', 'PUT'])
def req_show(wid):
    if request.method == 'PUT':
        return 201
    else:
        show = get_show(wid)
        m = show.make()
        return jsonify(m)


@app.route('/thalia/shows')
def req_all_shows():
    all_shows = get_all_shows()
    m = map(lambda x: x.make(), all_shows)
    return jsonify(m)


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('req_show', wid=31))
