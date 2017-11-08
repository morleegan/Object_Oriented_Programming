from thalia.showinfo import ShowInfo
import datetime

showinfo = ShowInfo(web="http://test.com", date=datetime.date(2, 2, 2), time=datetime.time(1, 1, 1), name="test")


def test_create_show_info():
    sinfo = ShowInfo(date=datetime.date(2, 2, 2), name="Annie", time=datetime.time, web='http://annie.com')
    assert sinfo is not None


# def test_make_show_info():
#     assert showinfo.make_json() == {
#         "name": "test",
#         "web": "http://test.com",
#         "date": datetime.date(2, 2, 2),
#         "time": datetime.time(1, 1, 1)
#     }


if __name__ == '__main__':
    # test_make_show_info()
    test_create_show_info()