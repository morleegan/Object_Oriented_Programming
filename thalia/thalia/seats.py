import uuid


class Seat:
    """Seat class: """
    def __init__(self, seat=None):
        """Initializing Seat class: this is a single chair, created as a linked list"""
        self.__cid = uuid.uuid4().hex     # all ids will be stored in hex form to make comparisons easier
        self.__name = seat               # chair name
        self.l_seat = None
        self.r_seat = None
        self.__status = "available"       # available and sold

    def check_availability(self):
        """checks for seat availability """
        if self.__status == "available":
            return True
        return False

    def bought_seat(self):
        """change status to sold"""
        self.__status = "sold"

    def get_name(self):
        return self.__name

    def get_cid(self):
        return self.__cid

    def get_status(self):
        return self.__status
