
class Seat:
    """Seat class: """
    def __init__(self, **kws):
        """Initializing Seat class: this is a single chair, created as a linked list"""
        self.cid = None
        self.l_cid = None
        self.r_cid = None
        self.status = "available"

        for opt in ['cid', 'l_cid', 'r_cid']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def next_seat(self, next_seat):
        """checks if the next seat is available and next to seat used"""
        if self.r_cid == next_seat.cid:
            if self.is_available():
                return True
        return False

    def is_available(self):
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
            "seat": self.cid,
            "status": self.status
        }