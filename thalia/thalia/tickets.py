import uuid


class Ticket:
    """Ticket class """
    def __init__(self, show=None, patron=None):
        self.__tid = uuid.uuid4().hex
        self.__show = show
        self.__patron = patron

    def get_tid(self):
        return self.__tid

    def get_show(self):
        return self.__show

    def get_patron(self):
        return self.__patron

