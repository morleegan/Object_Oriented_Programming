import uuid

# from thalia.utilities.connect import ApiCalls


class Sections:
    """Section class: holds seats and row values"""

    def __init__(self, **kws):
        """Initialization of Section Class"""
        # ApiCalls.__init__(self)
        self.sid = uuid.uuid4()                 # id of section
        self.name = None                        # section name
        self.price = None                       # price of section
        self.row = None                         # list of row classes
        self.status = "ok"

        for opt in ['sid', 'price','row']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

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

    def make_sections(self):
        m = {
            "sid": self.sid,
            "price": self.price
        }
        return m

    def make_json(self):
        return {
            "sid": self.sid,
            "seating": list(map(lambda r: r.make_json(), self.row)) if self.row else None
        }


