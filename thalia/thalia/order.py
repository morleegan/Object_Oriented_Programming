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

    def make_json(self):
        return {
            "wid": self.show.wid,
            "section": self.show.seating_info.sid,
            "seats": list(map(lambda seat: {"cid": seat.cid, "seat": seat.seat}, self.show.seating_info.row.seats)),
            "patron_info": self.ordered_by
        }


class Patron:
    """Patron class"""
    def __init__(self):
        self.name = None
        self.phone = None
        self.email = None
        self.billing_address = None
        self.cc_number = None
