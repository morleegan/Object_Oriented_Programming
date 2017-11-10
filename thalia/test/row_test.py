from thalia.row import Row

row1 = Row(row=1, seats=[1, 2, 3, 4, 5])


def test_get_row_number():
    assert row1.get_name() == 1


def test_search_row():
    s = row1.get_seats()
    s2 = s.r_seat
    sid = s.get_cid()
    assert s == row1.search_row(sid)
    assert s2 == row1.search_row(s2.get_cid())
    assert row1.search_row(1) is None


def test_find_seats():
    test1 = row1.find_seats(3)
    assert test1[0].get_name() == 5
    assert test1[1].get_name() == 4
    assert test1[2].get_name() == 3
    assert row1.find_seats(8) is None


def test_get_as_list():
    assert row1.get_seats_as_list() == [1,2,3,4,5]

if __name__ == '__main__':
    test_get_row_number()
    test_search_row()
    test_find_seats()
    test_get_as_list()
