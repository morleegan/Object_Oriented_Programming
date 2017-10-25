import unittest

from thalia.seatingClass import Sections

sec_test = Sections(seats={'A': [1, 2, 3, 4, 5, 6],
                           'B': [7, 8, 9, 10, 11, 12]})

sec_test1 = Sections(seats={'A': [1, 2, 3, 5, 6],
                            'B': [7, 8, 9, 10, 11, 12]})


def test_find_seat_success():
    assert sec_test.find_seats(5) == [1, 2, 3, 4, 5]
    assert sec_test1.find_seats(5) == [7, 8, 9, 10, 11]


def test_find_seats_fail():
    assert sec_test.find_seats(8) is None


if __name__ == '__main__':
    test_find_seat_success()
