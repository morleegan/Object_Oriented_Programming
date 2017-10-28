from thalia.show import Show
from thalia.show import ShowInfo
from thalia.section import Sections
import datetime

seatinginfo = Sections(sid=1, price=2)
showinfo = ShowInfo(web="http://test.com", date=datetime.date(2, 2, 2), time=datetime.time(1, 1, 1), name="test")
show1 = Show(wid=2, seating_info=seatinginfo, show_info=showinfo)


def test_create_show_info():
    sinfo = ShowInfo(date=datetime.date(2, 2, 2), name="Annie", time=datetime.time, web='http://annie.com')
    assert sinfo is not None


def test_create_show():
    sinfo = ShowInfo(date=datetime.date(2, 2, 2), name="Annie", time=datetime.time, web='http://annie.com')
    show = Show(show_info=sinfo)
    assert show is not None

def test_make_show():
    assert show1.make_json() == {
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
    assert seatinginfo.make_sections() == {
        "sid": 1,
        "price": 2
    }


def test_make_show_info():
    assert showinfo.mak_json() == {
        "name": "test",
        "web": "http://test.com",
        "date": datetime.date(2, 2, 2),
        "time": datetime.time(1, 1, 1)
    }

if __name__ == '__main__':
    test_create_show_info()
    test_create_show()
