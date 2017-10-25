import datetime


class Show:
    """Show class: overarching class"""

    def __init__(self, *args, **kws):
        """Initialization of show, contains show info"""
        self.wid = 0    # TODO: add implementation of getID
        self.seating_info = None
        self.show_info = None

        for opt in ['seating_info']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])


class ShowInfo:

    def __init__(self, *args, **kws):
        self.web = None
        self.name = None
        self.date = datetime.date(2, 2, 2)
        self.time = datetime.time()
        self.seating_info = None

        for opt in ['web', 'name', 'date', 'time']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])