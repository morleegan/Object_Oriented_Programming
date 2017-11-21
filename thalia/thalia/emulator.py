from thalia.venue import Theater
from thalia.show import Show
from thalia.showinfo import ShowInfo
from thalia.patron import Patron
from thalia.order import Orders
from thalia.tickets import Ticket

"""Main methods of the different actions taken by the REST"""


class Emulator:
    """Interface between Delivery and Thalia"""
    def __init__(self, shows=list(), orders=list(), donations=list()):
        self.shows = shows
        self.orders = orders
        self.theater = Theater()
        self.donations = donations
        self.tickets = list()
        self.used_tickets = list()

    def theater_json(self):
        """/seating"""
        return list(map(lambda x: {"sid": str(x.get_sid()), "section_name": x.get_name()}, self.theater.get_theater()))

    def show_json(self):
        """/show"""
        show_json = list()
        if self.shows:
            for show in self.shows:
                show_json.append({
                    "wid": show.get_wid(),
                    "show_info": Emulator.make_show_info(show.get_show_info())
                })
        return show_json

    def order_json(self):
        order_list = list()
        for order in self.orders:
            o = self.make_order(order)
            order_list.append(o)
        return order_list

    def donation_json(self):
        donate_list = list()
        for donation in self.donations:
            d = {
                "did": donation.get_did(),
                "wid": donation.get_wid(),
                "count": donation.get_ticket_amount(),
                "tickets": donation.get_assigned_tickets(),
                "status": donation.get_status(),
                "patron_info": Emulator.make_patron(donation.get_patron())
            }
            donate_list.append(d)
        return donate_list

    def ticket_by_id_json(self, tid=0):
        for ticket in self.tickets:
            if ticket.check_id(tid):
                return ticket

    def section_by_id_json(self, sid=0):
        """/sections/sid"""
        for section in self.theater.get_theater():
            if section.check_sid(sid):
                return {
                    "sid": str(section.get_sid()),
                    "section_name": section.get_name(),
                    "seating": list(map(lambda x: {"row": x.get_name(),
                                                   "seats": Emulator.seats_as_list(x.get_seats_as_list())},
                                        section.get_rows()))
                }

    def order_by_id_json(self, oid=0):
        for order in self.orders:
            if order.check_id(oid):
                ord_dict = self.make_order(order)
                ord_dict["tickets"] = Emulator.make_ticket_list(order.get_tickets())
                return ord_dict

    def show_by_id_json(self, wid=0):
        """show/wid"""
        for s in self.shows:
            if s.get_wid() == wid:
                return {
                    "wid": wid,
                    "show_info": Emulator.make_show_info(s.get_show_info()),
                    "seating_info": list(map(lambda x: {"sid": x.get_sid(), "price": x.get_price()}, s.get_seating_info()))
                }

    def show_by_section_json(self, wid=0):
        """GET shows by section with wid"""
        for s in self.shows:
            if s.check_wid(wid):
                return list(map(lambda x: {"sid": x.get_sid(), "section_name":x.get_name(),"price": x.get_price()},
                                s.get_seating_info()))

    def show_by_section_sid_json(self, wid=0, sid=0):
        """GET seating of section, wid, sid"""
        for show in self.shows:
            if show.check_wid(wid):
                for sec in show.get_seating_info():
                    if sec.check_sid(sid):
                        return {
                            "wid": wid,
                            "show_info": self.make_show_info(show.get_show_info()),
                            "sid": sid,
                            "section_name": sec.get_name(),
                            "price": sec.get_price(),
                            "seating": list(map(lambda x: {"row": x.get_name(), "seats":
                                            Emulator.seats_as_dict(x.get_seats_as_list())}, sec.get_rows()))
                        }

    def order_by_date(self, start, end):
        order_list = list()
        for order in self.orders:
            if order.check_date(start_date=start, end_date=end):
                o = self.make_order(order)
                order_list.append(o)
        return order_list

    def create_show(self, showinfo=None, seating=None):
        """show posted"""
        showinfo_obj = ShowInfo(name=showinfo['name'], web=showinfo['web'], date=showinfo['date'], time=showinfo['time'])
        theater = Theater()
        theater.create_seating(seating)
        new_show = Show(show_info=showinfo_obj, seating_info=theater.get_seating())
        self.shows.append(new_show)
        return {"wid": str(new_show.get_wid())}

    def create_order(self, content=None):
        """post order"""
        p_info = content['patron_info']
        patron = Patron(name=p_info['name'], phone=p_info['phone'], email=p_info['email'],
                        billing_address=p_info['billing_address'], cc_num=p_info['cc_number'],
                        cc_exp=p_info['cc_expiration_date'])
        show = self.show_by_section_sid_json(wid=content['wid'], sid=content['sid'])
        tickets = list(map(lambda x: Ticket(cid=x['cid'], seat=x['seat']), content['seats']))

        new_order = Orders(patron=patron, show=content['wid'], single_cost=show['price'], sid=content['sid'],
                           tickets=tickets)
        self.orders.append(new_order)
        self.tickets.append(tickets)
        return {
            "oid": new_order.get_oid(),
            "wid": content['wid'],
            "show_info": show['show_info'],
            "date_ordered": str(new_order.get_date_ordered()),
            "order_amount": new_order.get_ordered_price(),
            "tickets": list(map(lambda x: x.get_tid(), new_order.get_tickets()))
        }

    def use_ticket(self, content=None):
        for ticket in self.tickets:
            if ticket.check_id(content['tid']):
                ticket.change_status("used")

        return {"tid": content['tid'], "status": "used"}

    def update_show(self, wid=0, show_info=None, seating=None):
        """PUT shows with wid"""
        for s in self.shows:
            if s.check_wid(wid):
                s.get_show_info().update_showinfo(show_info)
                [x.set_price(y['price']) for x, y in zip(s.get_seating_info(), seating)]
                return 'success'

    def show_seats_request(self, wid=0, sid=0, count=0):
        for show in self.shows:
            if show.check_wid(wid):
                for sec in show.get_seating_info():
                    if sec.check_sid(sid):
                        seats = sec.find_seats(count)
                        json = {
                            "wid": wid,
                            "show_info": self.make_show_info(show.get_show_info()),
                            "sid": sid,
                            "section_name": sec.get_name(),
                            "starting_seat_id": None,
                            "status": sec.get_status(),
                            "seating": seats if seats else list(),
                        }
                        if seats:
                            json.update({"total_price": (sec.get_price() * count)})
                        return json

    """static methods used for creation"""

    @staticmethod
    def seats_as_list(seats):
        return sorted(list(map(lambda x: str(x.get_name()), seats)))

    @staticmethod
    def seats_as_dict(seats):
        return sorted(list(map(lambda x: {"cid": x.get_cid(), "seat": str(x.get_name()), "status": x.get_status()},
                               seats)), key=lambda x: x['seat'])

    @staticmethod
    def make_show_info(show_info):
        return {
            "name": show_info.get_name(),
            "web": show_info.get_web(),
            "date": str(show_info.get_date()).strip(' 00:00:00'),
            "time": str(show_info.get_time())
        }

    def make_order(self, order):
        show = self.show_by_id_json(order.get_wid())
        return {
            "oid": order.get_oid(),
            "wid": order.get_wid(),
            "show_info": show['show_info'],
            "date_ordered": str(order.get_date_ordered()),
            "number_of_tickets": order.get_number_of_tickets(),
            "patron_info": Emulator.make_patron(order.get_patron()),
        }

    @staticmethod
    def make_patron(patron):
        if patron:
            return {
                "name": patron.get_name(),
                "phone": patron.get_phone(),
                "email": patron.get_email(),
                "billing_address": patron.get_bill_adr(),
                "cc_number": patron.get_cc_num(),
                "cc_expiration_date": patron.get_cc_exp()
            }
        return patron

    @staticmethod
    def make_ticket_list(ticket):
        return list(map(lambda x: {"tid": x.get_tid(), "status": x.get_status()}, ticket))


