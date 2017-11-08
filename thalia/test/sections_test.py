from thalia.section import Sections
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
seat_list2 = [a, b, c, j, k, f, g, h]

row1 = Row(row='A', seats=seat_list)
row2 = Row(row='B', seats=seat_list1)
row3 = Row(row='C', seats=seat_list2)

sec_test = Sections(row=[row1], sid=1, price=2)
sec_test1 = Sections(row=[row1, row3], sid=1, price=2)
sec_test2 = Sections(row=[row3])


#tests for sections class

def test_find_seats():
    generator = sec_test.find_seats(3)
    assert next(generator) == [a, b, c]

    generator2 = sec_test2.find_seats(3)
    assert next(generator2) == [a, b, c]
    assert next(generator2) == [j, k, f]


def test_find_specific_success():
    assert sec_test1.find_specific_seats('C', 3) == [a, b, c]


def test_find_specific_fail():
    assert sec_test1.find_specific_seats('A', 6) is None
    # assert sec_test1.status == "Error: 6 contiguous seats not available"


# def test_make_show_section():
#     assert sec_test.make_sections() == {
#         "sid": 1,
#         "price": 2
#     }
#
#
# def test_make_json():
#     assert sec_test1.make_json() =={
#         "sid": 1,
#         "seating": [{
#             "row": 'A',
#             "seats": [1,2,3,4]
#         },
#             {
#             "row": 'C',
#             "seats": [1,2,3,4,5,6,7,8]
#         }]
#     }


if __name__ == '__main__':
    # test_find_seats()
    test_find_specific_success()
    test_find_specific_fail()
    # test_make_show_section()
    # test_make_json()

