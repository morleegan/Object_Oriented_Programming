from thalia.show import Show
from thalia.showinfo import ShowInfo
from thalia.section import Sections
import datetime

seatinginfo = Sections(sid=1, price=2)
showinfo = ShowInfo(web="http://test.com", date=datetime.date(2, 2, 2), time=datetime.time(1, 1, 1), name="test")
show1 = Show(seating_info=seatinginfo, show_info=showinfo)


def test_check_id_success():
    id = show1.get_wid()
    assert show1.check_id(id) is True


def test_check_id_fail():
    assert show1.check_id(3) is False


def test_create_show():
    sinfo = ShowInfo(date=datetime.date(2, 2, 2), name="Annie", time=datetime.time, web='http://annie.com')
    show = Show(show_info=sinfo)
    assert show is not None


if __name__ == '__main__':
    test_check_id_fail()
    test_check_id_success()
    # test_make_seating_info()
    test_create_show()
    # test_make_show()

