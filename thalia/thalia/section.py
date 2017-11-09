import uuid

# from thalia.utilities.connect import ApiCalls
from thalia.row import Row


class Sections:
    """Section class: holds seats and row values"""

    def __init__(self, wid=None, price=None, row=dict(), name=None):
        """Initialization of Section Class"""
        # ApiCalls.__init__(self)
        self.__wid = wid if wid else uuid.uuid4()   # id of section
        self.__name = name                          # section name
        self.__price = price                        # price of section
        self.__rows = list()                        # list of row classes
        self.__status = "ok"
        self.create_section(row)

    def get_wid(self):
        return self.__wid

    def get_rows(self):
        return self.__rows

    def get_status(self):
        return self.__status

    def get_price(self):
        return self.__price

    def set_status(self, new_status):
        self.__status = new_status

    def create_section(self, rows):
        if not self.__rows:
            row_list = list()
            for key, val in rows.items():
                r = Row(row=key, seats=val)
                row_list.append(r)
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
        """TODO: not in api"""
        pass
