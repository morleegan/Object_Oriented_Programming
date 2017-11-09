from thalia.seats import Seat

s1 = Seat(1)


def test_check_availability():
    assert s1.check_availability() is True
    s1.bought_seat()
    assert s1.check_availability() is False


def test_bought_seat():
    s1.bought_seat()
    assert s1.status == "sold"


if __name__ == '__main__':
    test_check_availability()
    test_bought_seat()
