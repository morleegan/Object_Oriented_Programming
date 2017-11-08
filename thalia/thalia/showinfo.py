import datetime


class ShowInfo:

    def __init__(self, **kws):
        self.web = None
        self.name = None
        self.date = datetime.date(2, 2, 2)
        self.time = datetime.time()

        for opt in ['web', 'name', 'date', 'time']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

