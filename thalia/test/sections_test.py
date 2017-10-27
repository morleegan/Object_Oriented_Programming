from thalia.section import Sections
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

sec_test = Sections(seats={'A': seat_list})

sec_test1 = Sections(seats={
    'A': seat_list,
    'B': seat_list1,
})

sec_test2 = Sections(seats={'A': seat_list2})


# tests for sections class
def test_find_seat_success():
    assert sec_test.find_seats(4) == [a, b, c, d]
    assert sec_test2.find_seats(5) == [j, k, f, g, h]


def test_find_seats_fail():
    assert sec_test.find_seats(8) is None


def test_find_specific_success():
    assert sec_test1.find_specific_seats('A', 3) == [a, b, c]
    assert sec_test1.find_specific_seats('B', 4) == seat_list1
    assert sec_test2.find_specific_seats('A', 5) == [j, k, f, g, h]


def test_find_specific_fail():
    assert sec_test1.find_specific_seats('A', 5) is None


if __name__ == '__main__':
    test_find_seat_success()
    test_find_seats_fail()
    test_find_specific_success()
    test_find_specific_fail()

