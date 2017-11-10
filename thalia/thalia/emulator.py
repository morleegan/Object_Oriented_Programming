import json
from thalia.venue import Theater
from thalia.show import Show
from thalia.showinfo import ShowInfo


class Emulator:
    """Interface between Delivery and Thalia"""
    def __init__(self):
        pass

    def make_json(self):
        pass


class SectionsEmulator(Emulator):
    """API Sections/Seating calls are turned into JSON here"""
    obj = Theater()

    def __init__(self):
        Emulator.__init__(self)
        self.sections = self.obj.get_theater()

    def make_json(self):
        return list(map(lambda x: {"sid": x.get_sid(), "section_name": x.get_name()}, self.sections))

    def make_section_by_id(self, sid):
        for s in self.sections:
            if str(s.get_sid()) == str(sid):
                return {
                    "sid": s.get_sid(),
                    "section_name": s.get_name(),
                    "seating": list(map(lambda x: {"row": x.get_name(), "seats": x.get_seats_as_list()}, s.get_rows()))
                }

    def make_seats_request(self, wid, sid, count):
        return {
            "wid": wid,
            "show_info": {},
            "sid": sid,
            "section_name": None,
            "starting_seat_id": None,
            "status": "ok",
            "total_amount": count,
            "seating": [],
        }


class ShowEmulator(Emulator):
    """API connection creates JSON for show"""

    def __init__(self, show=None):
        Emulator.__init__(self)
        showinfo = ShowInfo()
        self.show = Show(show_info=showinfo)

    def make_json(self):
        return {
            "wid": self.show.get_wid(),
            "show_info": self.make_show_info(self.show.show_info)
        }

    @staticmethod
    def make_show_info(show_info):
        return {
            "name": show_info.get_name(),
            "web": show_info.get_web(),
            "date": str(show_info.get_date()).strip(' 00:00:00'),
            "time": str(show_info.get_time())
        }
