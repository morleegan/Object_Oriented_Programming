from thalia.seats import Seat

s1 = Seat(seat=1)
s2 = Seat(seat=2)
s3 = Seat(seat=3)
s4 = Seat(seat=4)
s1.r_seat = s2
s2.r_seat = s4
s3.r_seat = s3


def test_next_to_success():
    assert s1.next_seat(s2) is True


def test_next_to_fail():
    assert s3.next_seat(s4) is False
    s1.bought_seat()
    assert s1.next_seat(s2) is False


def test_make_json():
    assert s2.make_json() == {
        "seat": 2,
        "status": "available"
    }


def test_bought_seat():
    s1.bought_seat()
    assert s1.status == "sold"


if __name__ == '__main__':
    test_next_to_success()
    test_next_to_fail()
    test_bought_seat()
    test_make_json()
