from thalia.seats import Seat

s1 = Seat(cid=1, l_cid=0, r_cid=2)
s2 = Seat(cid=2, l_cid=1, r_cid=3)
s3 = Seat(cid=1, l_cid=0, r_cid=4)
s4 = Seat(cid=2, l_cid=5, r_cid=3)


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
