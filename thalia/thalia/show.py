import datetime


class Show:
    """Show class: overarching class"""

    def __init__(self, **kws):
        """Initialization of show, contains show info"""
        self.wid = 0        # TODO: add implementation of getID
        self.seating_info = None
        self.show_info = None

        for opt in ['wid', 'seating_info', 'show_info']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def check_id(self, wid):
        if self.wid == wid:
            return True
        return False

    def make(self):
        m = {
            "wid": self.wid,
            "show_info": self.show_info.make(),
            "seating_info": self.seating_info.make_sections()
        }
        return m


class ShowInfo:

    def __init__(self, **kws):
        self.web = None
        self.name = None
        self.date = datetime.date(2, 2, 2)
        self.time = datetime.time()

        for opt in ['web', 'name', 'date', 'time']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def make(self):
        m = {
            "name": self.name,
            "web": self.web,
            "date": self.date,
            "time": self.time
        }
        return m
