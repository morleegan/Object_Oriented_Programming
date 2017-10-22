import datetime


class ShowClass:
    """Show class: overarching class"""

    def __init__(self, *args, **kws):
        """Initialization of show, contains show info"""
        self.web = None
        self.wid = 0    # TODO: add implementation of getID
        self.name = None
        self.date = datetime.date(2, 2, 2)
        self.time = datetime.time()

        for opt in ['web', 'name', 'date', 'time']:
            if opt in args:
                setattr(self, opt, kws[opt])




