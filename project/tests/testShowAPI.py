# Third-party imports...
import httpretty
import json

# Local imports...
from src.api.show import ShowApi

test_response = [
      {
        "wid": "307",
        "show_info": {
          "name": "King Lear",
          "web": "http://www.example.com/shows/king-lear",
          "date": "2017-12-04",
          "time": "19:00"
        }
      },
      {
        "wid": "308",
        "show_info": {
          "name": "King Lear",
          "web": "http://www.example.com/shows/king-lear",
          "date": "2017-12-05",
          "time": "13:00"
        }
      },
    ]

test_response2 = {
        "wid": "309",
        "show_info": {
          "name": "King Lear",
          "web": "http://www.example.com/shows/king-lear",
          "date": "2017-12-05",
          "time": "19:00"
        }
      }


def test_req_view_all():
    httpretty.enable()
    json_test = json.dumps(test_response)
    sAPI_test = ShowApi()
    httpretty.register_uri(httpretty.GET, sAPI_test.url, status=200,
                           body=json_test)
    response = sAPI_test.req_view_all()

    assert response.status_code == 200
    assert response.json() == test_response

    httpretty.disable()


def test_req_view_spec_success():
    httpretty.enable()
    json_test = json.dumps(test_response2)
    sAPI_test = ShowApi()
    httpretty.register_uri(httpretty.GET, sAPI_test.url + str(309), status=200, body=json_test)
    response = sAPI_test.req_view(309)

    assert response.status_code == 200
    assert response.json() == test_response2

    httpretty.disable()


def test_req_view_spec_failure():
    httpretty.enable()
    sAPI_test = ShowApi()
    httpretty.register_uri(httpretty.GET, sAPI_test.url + str(308), status=404)
    response = sAPI_test.req_view(308)

    assert response.status_code == 404

    httpretty.disable()


def test_req_create():
    httpretty.enable()
    json_test = json.dumps(test_response2)
    sAPI_test = ShowApi()
    httpretty.register_uri(httpretty.POST, sAPI_test.url, status=200, body=json_test)
    response = sAPI_test.req_create()

    assert response.status_code == 200


if __name__ == '__main__':
    test_req_view_all()
    test_req_view_spec_success()
    test_req_view_spec_failure()
