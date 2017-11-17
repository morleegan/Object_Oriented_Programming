from datetime import date, time

from thalia.emulator import ShowEmulator
from thalia.showinfo import ShowInfo
from thalia.show import Show


showinfo = ShowInfo(name="test", web="test", date=date(day=1, month=1, year=2010), time=time())
show = Show(show_info=showinfo)
shows = list()
shows.append(show)
show_emu_test = ShowEmulator(shows=shows)
post = {
    "show_info": {
      "name": "King Lear",
      "web": "http://www.example.com/shows/king-lear",
      "date": "2017-12-05",
      "time": "13:00"
    },
    "seating_info": [
      {
        "sid": "123",
        "price": 600
      },
      {
        "sid": "124",
        "price": 75
      },
      {
        "sid": "125",
        "price": 60
      }
    ]
  }


def test_make_json():
    s = show_emu_test.make_json()
    assert isinstance(s, list)
    assert sorted(s[0].keys()) == sorted(['wid', 'show_info'])


def test_make_show_info():
    s = show_emu_test.make_show_info(showinfo)
    assert isinstance(s, dict)
    assert sorted(s.keys()) == sorted(['name', 'web', 'date', 'time'])


def test_make_object():
    s = show_emu_test.make_object(post)
    assert sorted(s.keys()) == ['wid']


if __name__ == '__main__':
    test_make_json()
    test_make_show_info()
    test_make_object()