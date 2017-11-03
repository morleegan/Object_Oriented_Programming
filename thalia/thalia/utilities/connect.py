from thalia.show import Show
from thalia.order import Orders
from thalia.section import Sections


class ApiCalls:
    def __init__(self):
        pass

    def make_json(self):
        return None


class Connection:
    """Class used as the interface between rest and oo
    Every class that can be called with REST should have this as a superclass
    """
    def __init__(self):
        pass

    @staticmethod
    def give_json(obj):
        """to give flask the data from background, it will call give json"""
        api_types = [Show, Orders, Sections]
        for t in api_types:
            if isinstance(obj, t):
                return obj.make_json()


