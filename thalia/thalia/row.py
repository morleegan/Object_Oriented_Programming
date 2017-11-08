class Row:
    """Row Class: """
    def __init__(self, **kws):
        self.row = None     # row number
        self.seats = None   # list of seats

        for opt in ['row', 'seats']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def seat_order(self, req_num):
        """creates a list of seats next to each other"""
        seat_order = []
        for i in range(0, len(self.seats) - 1):
            if self.seats[i].next_seat(self.seats[i + 1]):
                if not seat_order:
                    seat_order.append(self.seats[i])
                seat_order.append(self.seats[i + 1])
            else:
                seat_order = []
            # check for success
            if len(seat_order) == req_num:
                return seat_order


