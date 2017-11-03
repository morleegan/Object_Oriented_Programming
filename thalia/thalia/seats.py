import uuid


class Seat:
    """Seat class: """
    def __init__(self, **kws):
        """Initializing Seat class: this is a single chair, created as a linked list"""
        self.cid = uuid.uuid4().hex     # all ids will be stored in hex form to make comparisons easier
        self.seat = None                # chair name
        self.l_seat = None
        self.r_seat = None
        self.status = "available"       # available and sold

        for opt in ['l_seat', 'r_seat', 'seat']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def next_seat(self, next_seat):
        """checks if the next seat is available and next to seat used"""
        if self.r_seat.cid == next_seat.cid:
            if self.check_availability():
                return True
        return False

    def check_availability(self):
        """checks for seat availability """
        if self.status == "available":
            return True
        return False

    def bought_seat(self):
        """change status to sold"""
        self.status = "sold"

    def make_json(self):
        """creates json dict for api usage"""
        return {
            "seat": self.seat,
            "status": self.status
        }


