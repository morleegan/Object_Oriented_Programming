import uuid
import datetime

# from thalia.utilities.connect import Connection


class Orders:
    """Order Class"""
    def __init__(self, show=None, ticket_num=0):
        # Connection.__init__(self)
        self.oid = uuid.uuid4()
        self.show = show                                    # keep class
        self.date_ordered = datetime.date, datetime.time    # tuple
        self.ordered_amount = self.ordered_amount_init()    # calculate amount
        self.number_of_tickets = ticket_num                 # given at init
        self.ordered_by = None                              # patron info

    def ordered_amount_init(self):
        return self.number_of_tickets * self.show.seating_info.price


class Patron:
    """Patron class"""
    def __init__(self):
        self.name = None
        self.phone = None
        self.email = None
        self.billing_address = None
        self.cc_number = None
