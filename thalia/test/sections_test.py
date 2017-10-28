from thalia.section import Sections
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
seat_list2 = [a, b, c, j, k, f, g, h]

row1 = Row(row='A', seats=seat_list)
row2 = Row(row='B', seats=seat_list1)
row3 = Row(row='C', seats=seat_list2)

sec_test = Sections(row=[row1], sid=1, price=2)
sec_test1 = Sections(row=[row1, row3], sid=1, price=2)
sec_test2 = Sections(row=[row3])


# tests for sections class
def test_find_seats():
    assert sec_test.find_seats(3) == [a, b, c]
    assert sec_test1.find_seats(5) == [a, b, c, j, k]


def test_find_specific_success():
    assert sec_test1.find_specific_seats('C', 3) == [a, b, c]


def test_find_specific_fail():
    assert sec_test1.find_specific_seats('A', 6) is None


def test_make_show_section():
    assert sec_test.make_sections() == {
        "sid": 1,
        "price": 2
    }


def test_make_json():
    assert sec_test1.make_json() =={
        "sid": 1,
        "seating": [{
            "row": 'A',
            "seats": [1,2,3,4]
        },
            {
            "row": 'C',
            "seats": [1,2,3,4,5,6,7,8]
        }]
    }


if __name__ == '__main__':
    test_find_seats()
    test_find_specific_success()
    test_find_specific_fail()
    test_make_show_section()
    test_make_json()

