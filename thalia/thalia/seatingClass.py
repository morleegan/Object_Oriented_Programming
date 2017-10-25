

class Sections:
    """Section class: holds seats and row values"""
    def __init__(self, *args, **kws):
        """Initialization of Section Class"""
        self.sid = None
        self.price = None
        self.row = []           # list of value names, ex. A, B.. or 1, 2
        self.seats = dict()     # dictionary of lists, row name is key, seats as values

        for opt in ['sid', 'price', 'seats', 'row']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def find_seats(self, req_num):
        """right now it looks at a dictionary"""
        # TODO: check if seat is to left in seat struct, (after creating a seat struct)
        seat_order = []
        for row in self.seats:
            seat_order = []
            for i in range(1, len(self.seats[row])):
                if (self.seats[row][i-1]+1) == (self.seats[row][i]):
                    if not seat_order:
                        seat_order.append(self.seats[row][i-1])
                    seat_order.append(self.seats[row][i])
                else:
                    seat_order = []
                # check for success
                if len(seat_order) == req_num:
                    return seat_order


class Seat:
    """Seat class: """
    def __init__(self, *args, **kws):
        """Initializing Seat class"""
        self.cid = None
        self.l_cid = None
        self.r_cid = None
