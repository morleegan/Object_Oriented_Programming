from flask import Blueprint, request

report = Blueprint('report', __name__)


@report.route('/', methods=['GET'])
def req_view():
    return "report index"


@report.route('/<mrid>', methods=['GET'])
def req_report(mrid):
    # ?show={wid} | ?start_date=YYYYMMDD&end_date=YYYYMMDD
    wid = request.args.get('show', type=int)
    start = request.args.get('start_date', type=str)    # TODO: will have to parse
    end = request.args.get('end_date', type=str)
    return "start: " + start
