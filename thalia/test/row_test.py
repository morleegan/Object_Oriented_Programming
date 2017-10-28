from thalia.row import Row
from thalia.seats import Seat

a = Seat(cid=1, r_cid=2)
b = Seat(cid=2, l_cid=1, r_cid=3)
c = Seat(cid=3, l_cid=2, r_cid=4)
d = Seat(cid=4, l_cid=3)

e = Seat(cid=5, r_cid=6)
f = Seat(cid=6, l_cid=5, r_cid=7)
g = Seat(cid=7, l_cid=6, r_cid=8)
h = Seat(cid=8, l_cid=7)

j = Seat(cid=4, l_cid=3, r_cid=5)
k = Seat(cid=5, l_cid=4, r_cid=6)

seat_list = [a, b, c, d]
seat_list1 = [e, f, g, h]
seat_list2 = [a, b, j, k, f, g, h]

row1 = Row(row='A', seats=seat_list)
row2 = Row(row='B', seats=seat_list2)


def test_make_json():
    assert row1.make_json() == {
        "row": 'A',
        "seats": [1, 2, 3, 4]
    }


def test_seat_order_exists():
    assert row1.seat_order(3) == [a, b, c]
    j.bought_seat()
    assert row2.seat_order(4) == [k, f, g, h]


def test_seat_order_fail():
    assert row1.seat_order(5) is None


if __name__ == '__main__':
    test_make_json()
    test_seat_order_exists()
    test_seat_order_fail()
