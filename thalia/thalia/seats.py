
class Seat:
    """Seat class: """
    def __init__(self, **kws):
        """Initializing Seat class"""
        self.cid = None
        self.l_cid = None
        self.r_cid = None
        for opt in ['cid', 'l_cid', 'r_cid']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def next_to(self, next_seat):
        if self.r_cid == next_seat.cid:
            return True
        return False
