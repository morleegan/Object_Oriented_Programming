import uuid

# from thalia.utilities.connect import ApiCalls
from thalia.row import Row


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Theater(metaclass=Singleton):
    """Theater/Seating section."""

    def __init__(self, *args, **kwargs):
        self.sections = list()
        self.theater = dict()

        for opt in ['theater']:
            if opt in kwargs.keys():
                setattr(self, opt, kwargs[opt])

        self.create_theater(self.theater)

    def create_theater(self, theater):
        """theater is a list of"""
        for section in theater:
            new_seating = Sections(name=section['section_name'], row=section['seating'])
            self.sections.append(new_seating)


class Sections:
    """Section class: holds seats and row values"""

    def __init__(self, **kwargs):
        """Initialization of Section Class"""
        # ApiCalls.__init__(self)
        self.sid = uuid.uuid4()                 # id of section
        self.name = None                        # section name
        self.price = None                       # price of section
        self.row = None                         # list of row classes
        self.status = "ok"

        for opt in ['sid', 'price', 'row']:
            if opt in kwargs.keys():
                setattr(self, opt, kwargs[opt])

    def find_seats(self, req_num):
        """find seats for order"""
        for r in self.row:
            return r.seat_order(req_num)

        self.status = "Error: " + str(req_num) + " contiguous seats not available"

    def find_specific_seats(self, row_num, req_num):
        """find seats when the row is given"""
        for r in self.row:
            if r.row == row_num:
                return r.seat_order(req_num)
