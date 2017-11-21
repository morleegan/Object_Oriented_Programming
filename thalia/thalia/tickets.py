import uuid


class Ticket:
    """Ticket class """
    def __init__(self, cid=None, seat=None):
        self.__tid = uuid.uuid4().hex
        self.__status = "active"
        self.__cid = cid
        self.__seat = seat

    def get_tid(self):
        return self.__tid

    def get_seat(self):
        return self.__seat

    def get_status(self):
        return self.__status

    def change_status(self, status):
        self.__status = status

    def check_id(self, tid):
        if self.get_tid() == tid:
            return True
        return False


