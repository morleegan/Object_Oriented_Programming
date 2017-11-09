import uuid


class Seat:
    """Seat class: """
    def __init__(self, seat=None):
        """Initializing Seat class: this is a single chair, created as a linked list"""
        self.cid = uuid.uuid4().hex     # all ids will be stored in hex form to make comparisons easier
        self.seat = seat               # chair name
        self.l_seat = None
        self.r_seat = None
        self.status = "available"       # available and sold

    def check_availability(self):
        """checks for seat availability """
        if self.status == "available":
            return True
        return False

    def bought_seat(self):
        """change status to sold"""
        self.status = "sold"

