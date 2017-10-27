from thalia.show import Show
from thalia.show import ShowInfo
import datetime


def test_create_show_info():
    sinfo = ShowInfo(date=datetime.date(2, 2, 2), name="Annie", time=datetime.time, web='http://annie.com')
    assert sinfo is not None


def test_create_show():
    sinfo = ShowInfo(date=datetime.date(2, 2, 2), name="Annie", time=datetime.time, web='http://annie.com')
    show = Show(show_info=sinfo)
    assert show is not None


if __name__ == '__main__':
    test_create_show_info()
    test_create_show()
