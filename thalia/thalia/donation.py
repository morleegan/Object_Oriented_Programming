from uuid import uuid4


class Donation:
    """Donation class"""
    def __init__(self, wid=0, count=0, patron_info=None):
        self.__did = uuid4().hex                # donation id to be returned to user
        self.__wid = wid                        # show id for tickets they are waiting on
        self.__count = count                    # ticket #
        self.__patron = patron_info             # patron info
        self.__status = "pending"               # status of assigned seats
        self.__ticket_assigned = list()         # list of tid assigned

    def get_did(self):
        return self.__did

    def get_wid(self):
        return self.__wid

    def get_ticket_amount(self):
        return self.__count

    def get_patron(self):
        return self.__patron

    def get_status(self):
        return self.__status

    def get_assigned_tickets(self):
        return self.__ticket_assigned

    def update_status(self, new_status):
        self.__status = new_status

    def update_assigned_tickets(self, tids=None):
        if tids:
            self.__ticket_assigned.append(tids)
            self.update_status("assigned")



