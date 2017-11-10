import uuid
# from thalia.utilities.connect import ApiCalls
from thalia.row import Row


class Sections:
    """Section class: holds seats and row values"""

    def __init__(self, sid=None, price=None, row=list(), name=None):
        """Initialization of Section Class"""
        self.__sid = sid if sid else uuid.uuid4().hex  # id of section
        self.__name = name                          # section name
        self.__price = price                        # price of section
        self.__rows = list()                        # list of row classes
        self.__status = "ok"
        self.create_section(row)

    def get_sid(self):
        return self.__sid

    def get_name(self):
        return self.__name

    def get_rows(self):
        return self.__rows

    def get_status(self):
        return self.__status

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def set_status(self, new_status):
        self.__status = new_status

    def check_sid(self, other_sid):
        if self.get_wid() == other_sid:
            return True
        else:
            return False

    def create_section(self, rows):
        if not self.__rows:
            row_list = list()
            for r in rows:
                # iterates through a list of dicts
                r_created = Row(row=r['row'], seats=r['seats'])
                row_list.append(r_created)
            self.__rows = row_list

    def find_seats(self, req_num):
        """find seats for order"""
        rows = self.get_rows()
        for r in rows:
            seats = r.find_seats(req_num)
            if seats:
                return seats

        err = "Error: " + str(req_num) + " contiguous seats not available"
        self.set_status(err)
        return None

    def find_specific_seats(self, list_cid):
        """ TODO: Not in API """
        return NotImplementedError
