from thalia.seats import Seat


def test_next_to_success():
    s1 = Seat(cid=1, l_cid=0, r_cid=2)
    s2 = Seat(cid=2, l_cid=1, r_cid=3)
    assert s1.next_to(s2) is True


def test_next_to_fail():
    s1 = Seat(cid=1, l_cid=0, r_cid=4)
    s2 = Seat(cid=2, l_cid=5, r_cid=3)
    assert s1.next_to(s2) is False


if __name__ == '__main__':
    test_next_to_success()
    test_next_to_fail()
