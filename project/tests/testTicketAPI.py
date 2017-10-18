# Third-party imports...
import httpretty
import json

# Local imports...
from src.api.ticket import TicketApi


def test_req_view_all():
    httpretty.enable()

    json_body = json.dumps({'tid': ['1', '2', '3']})
    tAPI_test = TicketApi()
    httpretty.register_uri(httpretty.GET, tAPI_test.url, status=200,
                           body=json_body)
    response = tAPI_test.req_view_all()

    assert response.status_code == 200
    assert response.json() == {'tid': ['1', '2', '3']}

    httpretty.disable()


def test_req_view():
    # need design of API for tickets
    return NotImplementedError


if __name__ == '__main__':
    test_req_view_all()

