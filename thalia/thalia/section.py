class Sections:
    """Section class: holds seats and row values"""

    def __init__(self, **kws):
        """Initialization of Section Class"""
        self.sid = None
        self.price = None
        self.row = []           # list of value names, ex. A, B.. or 1, 2
        self.seats = dict()     # dictionary of lists, row name is key, seats as values

        for opt in ['sid', 'price', 'seats', 'row']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def find_seats(self, req_num):
        """find seats for order"""
        for r, s in self.seats.items():
            seat_order = []
            for i in range(0, len(s)-1):
                if s[i].next_to(s[i+1]):
                    if not seat_order:
                        seat_order.append(s[i])
                    seat_order.append(s[i+1])
                else:
                    seat_order = []
                # check for success
                if len(seat_order) == req_num:
                    return seat_order

    def find_specific_seats(self, row, req_num):
        """find seats when the row is given"""
        s = self.seats[row]
        seat_order = []
        for i in range(0, len(s)-1):
            if s[i].next_to(s[i+1]):
                if not seat_order:
                    seat_order.append(s[i])
                seat_order.append(s[i+1])
            else:
                seat_order = []
            # check for success
            if len(seat_order) == req_num:
                return seat_order

    def make(self):
        m = {
            "sid": self.sid,
            "price": self.price
        }
        return m