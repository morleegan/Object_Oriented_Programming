import datetime

from thalia.section import Sections
from thalia.show import Show, ShowInfo

seatinginfo = Sections(sid=1, price=2)
showinfo = ShowInfo(web="http://test.com", date=datetime.date(2, 2, 2), time=datetime.time(1, 1, 1), name="test")
show1 = Show(wid=2, seating_info=seatinginfo, show_info=showinfo)


def test_make_show():
    assert show1.make() == {
        "wid": 2,
        "show_info": {
            "name": "test",
            "web": "http://test.com",
            "date": datetime.date(2, 2, 2),
            "time": datetime.time(1, 1, 1)
        },
        "seating_info": {
            "sid": 1,
            "price": 2
        }
    }


def test_make_seating_info():
    assert seatinginfo.make() == {
        "sid": 1,
        "price": 2
    }


def test_make_show_info():
    assert showinfo.make() == {
        "name": "test",
        "web": "http://test.com",
        "date": datetime.date(2, 2, 2),
        "time": datetime.time(1, 1, 1)
    }


if __name__ == '__main__':
    test_make_show()
    test_make_seating_info()
    test_make_show_info()