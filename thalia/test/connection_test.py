from thalia.utilities.connect import ApiCalls, Connection

from thalia.section import Sections


def create_apicall():
    apicall = ApiCalls()
    assert apicall is not None


def test_give_json():
    section = Sections(sid=1, price=2)
    assert Connection.give_json(section) == {
        "sid": 1,
        "seating": None
    }


if __name__ == '__main__':
    test_give_json()
    create_apicall()