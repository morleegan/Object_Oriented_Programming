from thalia.section import Sections
from thalia.row import Row

# tests for sections class

s = Sections(name='main', price=80)
test_wid = 12
test_price = 21
test = [{'row': '1',
        'seats': ['1', '2', '3', '4', '5']}]


def test_create_section():
    s.create_section(test)
    s_row = s.get_rows()
    assert s_row[0].get_name() == str(1)


def test_get_rows():
    s2 = Sections(sid=test_wid, price=test_price, row=test)
    s_row = s2.get_rows()
    assert s_row[0].get_name() == str(1)


def test_get():
    s2 = Sections(sid=test_wid, price=test_price)
    assert 12 == s2.get_sid()
    assert test_price == s2.get_price()


def test_find_seats():
    s2 = Sections(sid=test_wid, price=test_price, row=test)
    seats = s2.find_seats(2)
    assert seats is not None
    assert seats[0].get_name() == '5'


def test_find_seats_fail():
    s2 = Sections(sid=test_wid, price=test_price, row=test)
    seats = s2.find_seats(6)
    assert seats is None
    assert s2.get_status() == "Error: 6 contiguous seats not available"


def test_check_sid():
    s2 = Sections(sid=1)
    assert s2.check_sid(1)


if __name__ == '__main__':
    test_create_section()
    test_get()
    test_get_rows()
    test_find_seats()
    test_find_seats_fail()

