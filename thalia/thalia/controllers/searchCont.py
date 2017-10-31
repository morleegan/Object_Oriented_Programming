from flask import Blueprint, request

search = Blueprint('search', __name__)


@search.route('/search', methods=['GET'])
def req_report():
    # search?topic=topicword&key=keyword
    topic = request.args.get('topicword', type=str)
    key = request.args.get('keyword', type=str)
    return "keyword and topic: " + key + " " + topic
