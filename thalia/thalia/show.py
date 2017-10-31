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

    def make_json(self):
        m = {
            "wid": self.wid,
            "show_info": self.show_info.make_json(),
            "seating_info": self.seating_info.make_sections()
        }
        return m

