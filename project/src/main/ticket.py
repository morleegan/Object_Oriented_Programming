
class Ticket:
    """what patrons can look up/buy"""
    def __init__(self, seat, row):
        self.row = row
        self.seat = seat

    def get_price(self):
        return self.price


class Person:
    """Person can we interface of employees/buyers eventually"""
    def __init__(self, name):
        self.name = name
