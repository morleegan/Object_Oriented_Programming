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


    # def make_json(self):
    #     return {
    #         "wid": self.show.wid,
    #         "section": self.show.seating_info.sid,
    #         "seats": list(map(lambda seat: {"cid": seat.cid, "seat": seat.seat}, self.show.seating_info.row.seats)),
    #         "patron_info": self.ordered_by
    #     }
    #
    # def make_json(self):
    #     """return json to use in api"""
    #     return {
    #         "row": self.row,
    #         "seats": list(map(lambda s: s.seat, self.seats))
    #     }
    #
    #
    # def make_json(self):
    #     """creates json dict for api usage"""
    #     return {
    #         "seat": self.seat,
    #         "status": self.status
    #     }
    #
    #
    # # considering moving this to a different place, json creation should be in a different section #
    #
    # def make_sections(self):
    #     m = {
    #         "sid": self.sid,
    #         "price": self.price
    #     }
    #     return m
    #
    # def make_json(self):
    #     return {
    #         "sid": self.sid,
    #         "seating": list(map(lambda r: r.make_json(), self.row)) if self.row else None
    #     }
    #
    # def make_seating(self):
    #     return {
    #         "section_name": self.name,
    #         "seating": list(map(lambda x: x.make_json(), self.row)) if self.row else None
    #     }
    #
    #
    # def make_json(self):
    #     m = {
    #         "name": self.name,
    #         "web": self.web,
    #         "date": self.date,
    #         "time": self.time
    #     }
    #     return m
    #
    # def make_json(self):
    #     m = {
    #         "wid": self.wid,
    #         "show_info": self.show_info.make_json(),
    #         "seating_info": self.seating_info.make_sections()
    #     }
    #     return m
    #

