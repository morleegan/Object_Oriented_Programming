from thalia.row import Row
from thalia.seats import Seat

a = Seat(seat=1)
b = Seat(seat=2)
c = Seat(seat=3)
d = Seat(seat=4)
a.r_seat = b
b.r_seat = c
c.r_seat = d

e = Seat(seat=5)
f = Seat(seat=6)
g = Seat(seat=7)
h = Seat(seat=8)
e.r_seat = f
f.r_seat = g
g.r_seat = h

j = Seat(seat=4)
k = Seat(seat=5)
j.r_seat = k
k.r_seat = f

seat_list = [a, b, c, d]
seat_list1 = [e, f, g, h]
seat_list2 = [a, b, j, k, f, g, h]

row1 = Row(row='A', seats=seat_list)
row2 = Row(row='B', seats=seat_list2)


# def test_make_json():
#     assert row1.make_json() == {
#         "row": 'A',
#         "seats": [1, 2, 3, 4]
#     }


def test_seat_order_exists():
    print(row1.seat_order(3))
    assert row1.seat_order(3) == [a, b, c]
    j.bought_seat()
    assert row2.seat_order(4) == [k, f, g, h]


def test_seat_order_fail():
    assert row1.seat_order(5) is None


if __name__ == '__main__':
    test_seat_order_exists()
    test_seat_order_fail()
