from thalia.seats import Seat


class Row:
    """Row Class: linked list implementation"""

    def __init__(self, row=None, seats=list()):
        self.__row = row                # row number
        self.__seats = None             # list of seats
        self.create_row(seats)          # creation of row

    def get_name(self):
        return self.__row

    def get_seats(self):
        return self.__seats

    def get_seats_as_list(self):
        seat_list = []
        r = self.get_seats()
        while r.r_seat is not None:
            seat_list.append(r.get_name())
            r = r.r_seat
        seat_list.append(r.get_name())
        return sorted(seat_list)

    def create_row(self, seat_list):
        """Creation of the linked list"""
        for s in seat_list:
            seat = Seat(seat=s)
            if self.__seats is None:
                self.__seats = seat
            else:
                seat.r_seat = self.__seats
                seat.r_seat.l_seat = seat
                self.__seats = seat

    def search_row(self, cid):
        """find cid in the row"""
        r = self.get_seats()
        if r is not None:
            while r.r_seat is not None:
                if r.get_cid() == cid:
                    return r
                r = r.r_seat
            if r.get_cid() == cid:
                return r
        return None

    def find_seats(self, num_req):
        """creates a order of seats for a num requested"""
        order = list()
        r = self.get_seats()
        while r.r_seat is not None:
            if r.check_availability():      # may need to look through orders to see if this is sold...
                order.append(r)
                if len(order) == num_req:
                    return order
            else:
                order = list()
            r = r.r_seat
        return None




