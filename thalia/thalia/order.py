import uuid
import datetime


class Orders:
    """Order Class"""
    def __init__(self, show=None, ticket_num=0, patron=None):
        self.__oid = uuid.uuid4()
        self.__show = show                                    # keep class
        self.__date_ordered = datetime.date, datetime.time    # tuple
        self.__ordered_amount = self.ordered_amount_init()    # calculate amount
        self.__number_of_tickets = ticket_num                 # given at init
        self.__ordered_by = patron                            # patron info

    def get_oid(self):
        return self.__oid

    def get_show(self):
        return self.__show

    def get_date_ordered(self):
        """:return tuple of date, time"""
        return self.__date_ordered

    def get_number_of_tickets(self):
        return self.__number_of_tickets

    def get_ordered_amount(self):
        return self.__ordered_amount

    def get_patron(self):
        return self.__ordered_by

    def ordered_amount_init(self):
        return self.__number_of_tickets * self.__show.seating_info.price

