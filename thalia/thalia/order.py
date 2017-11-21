import uuid
import datetime


class Orders:
    """Order Class"""
    def __init__(self, show=None, sid=0, single_cost=0, patron=None, tickets=list()):
        self.__oid = uuid.uuid4().hex
        self.__wid = show
        self.__sid = sid
        self.__tickets = tickets

        self.__date_ordered = datetime.datetime.today()
        self.__number_of_tickets = len(tickets)
        self.__ordered_by = patron
        self.__ordered_amount = self.calculate_cost(single_cost)

    def get_oid(self):
        return self.__oid

    def get_wid(self):
        return self.__wid

    def get_tickets(self):
        return self.__tickets

    def get_date_ordered(self):
        return self.__date_ordered

    def get_number_of_tickets(self):
        return self.__number_of_tickets

    def get_patron(self):
        return self.__ordered_by

    def get_ordered_price(self):
        return self.__ordered_amount

    def calculate_cost(self, single_cost):
        return self.get_number_of_tickets() * single_cost

    def check_id(self, tid):
        if self.get_oid() == tid:
            return True
        return False

    def check_date(self, start_date, end_date):
        start = datetime.datetime(year=int(start_date[:4]), month=int(start_date[4:6]), day=int(start_date[6:]))
        end = datetime.datetime(year=int(end_date[:4]), month=int(end_date[4:6]), day=int(end_date[6:]))

        if end > self.get_date_ordered() > start:
            return True
        return False

