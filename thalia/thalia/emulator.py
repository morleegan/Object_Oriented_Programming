from thalia.venue import Theater
from thalia.show import Show
from thalia.showinfo import ShowInfo


class Emulator:
    """Interface between Delivery and Thalia"""
    def __init__(self):
        pass

    def make_json(self):
        return NotImplemented

    def make_object(self):
        return NotImplemented


class TheaterEmulator(Emulator):
    """API Sections/Seating calls are turned into JSON here"""

    def __init__(self):
        Emulator.__init__(self)
        self.theater = Theater()

    def make_json(self):
        sections = self.theater.get_theater()
        return list(map(lambda x: {"sid": str(x.get_sid()), "section_name": x.get_name()}, sections))

    def make_section_by_id(self, sid=0):
        for section in self.theater.get_theater():
            if sid == str(section.get_sid()):
                return {
                    "sid": str(section.get_sid()),
                    "section_name": section.get_name(),
                    "seating": list(map(lambda x: {"row": x.get_name(), "seats": x.get_seats_as_list()},
                                        section.get_rows()))
                }
        return None

    def make_seats_request(self, sid, wid):
        # return {
        #     "wid": None,
        #     "show_info": {},
        #     "sid": None,
        #     "section_name": None,
        #     "starting_seat_id": None,
        #     "status": "ok",
        #     "total_amount": None,
        #     "seating": [],
        # }
        return NotImplemented


class ShowEmulator(Emulator):
    """API connection creates JSON for show"""

    def __init__(self, shows=list()):
        Emulator.__init__(self)
        self.shows = shows

    def make_json(self):
        show_json = list()
        if self.shows:
            for show in self.shows:
                show_json.append({
                    "wid": show.get_wid(),
                    "show_info": ShowEmulator.make_show_info(show.get_show_info())
                })
        return show_json

    def make_json_by_id(self, wid):
        for s in self.shows:
            if s.get_wid() == wid:
                return {
                    "wid": wid,
                    "show_info": self.make_show_info(s.get_show_info()),
                    "seating_info": list(map(lambda x: {"sid": x.get_sid(), "price": x.get_price()}, s.get_seating_info()))
                }

    @staticmethod
    def make_show_info(show_info):
        return {
            "name": show_info.get_name(),
            "web": show_info.get_web(),
            "date": str(show_info.get_date()).strip(' 00:00:00'),
            "time": str(show_info.get_time())
        }

    def make_object(self, obj=None, seating=None, showinfo=None):
        """POST show"""
        showinfo_obj = ShowInfo(name=showinfo['name'], web=showinfo['web'], date=showinfo['date'], time=showinfo['time'])
        theater = Theater()
        theater.create_seating(seating)
        new_show = Show(show_info=showinfo_obj, seating_info=theater.get_seating())
        self.shows.append(new_show)
        return {"wid": str(new_show.get_wid())}

    def update_object(self, wid=0, show_info=None, seating=None):
        """PUT shows with wid"""
        for s in self.shows:
            if s.check_wid(wid):
                s.get_show_info().update_showinfo(show_info)
                [x.set_price(y['price']) for x, y in zip(s.get_seating_info(), seating)]
                return 'success'

    def make_json_by_sections(self, wid):
        """GET shows by section with wid"""
        for s in self.shows:
            if s.check_wid(wid):
                return list(map(lambda x: {"sid": x.get_sid(),"section_name":x.get_name(),"price": x.get_price()},
                                s.get_seating_info()))

    def make_json_by_section_sid(self, wid, sid):
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
                            "seating": list(map(lambda x: {"row": x.get_name(), "seats": x.get_seats_as_list()},
                                                sec.get_rows()))
                        }


class PatronEmulator(Emulator):
    """API patron creates JSON"""
    def __init__(self):
        Emulator.__init__(self)

    @staticmethod
    def make_json(patron=None):
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


class OrderEmulator(Emulator):
    """API order creates JSON"""
    def __init__(self):
        Emulator.__init__(self)

    @staticmethod
    def make_json(order=None):
        if order:
            show = order.get_show()
            patron = order.get_patron()
            return {
                "oid": order.get_oid(),
                "wid": show.get_wid(),
                "show_info": ShowEmulator.make_show_info(show.get_showinfo()),
                "date_ordered": order.get_date_ordered(),
                "number_of_tickets": order.get_ticket_amount(),
                "patron_info": PatronEmulator.make_json(patron),

            }
        return order

    @staticmethod
    def make_json_w_oid(order=None):
        if order:
            before = OrderEmulator.make_json(order)
            ticket = order.get_tickets()
            before["tickets"] = list(map(lambda x: TicketEmulator.make_json(x), ticket))
            return before
        return order

    @staticmethod
    def make_post(order=None):
        if order:
            show = order.get_show()
            ticket = order.get_tickets()
            return {
                "oid": order.get_oid(),
                "wid": show.get_wid(),
                "show_info": ShowEmulator.make_show_info(show.get_showinfo()),
                "date_ordered": order.get_date_ordered(),
                "order_amount": order.get_order_amount(),
                "tickets": list(map(lambda x: {"ticket": x.get_name}, ticket))
            }

    @staticmethod
    def make_object(obj=None):
        return NotImplementedError


class DonationEmulator(Emulator):
    """API donation emulator"""
    def __init__(self):
        Emulator.__init__(self)

    @staticmethod
    def make_json(donation=None):
        """show.donations"""
        if donation:
            return {
                "did": donation.get_did(),
                "wid": donation.get_wid(),
                "count": donation.get_ticket_amount(),
                "tickets": donation.get_assigned_tickets(),
                "status": donation.get_status(),
                "patron_info": PatronEmulator.make_json(donation.get_patron())
            }
        return donation

    @staticmethod
    def make_post(did=None):
        if did:
            return {
                "did": did
            }


class TicketEmulator(Emulator):
    """API ticket"""
    def __init__(self):
        Emulator.__init__(self)

    @staticmethod
    def make_json(ticket=None):
        if ticket:
            return {"tid": ticket.get_tid(), "status": ticket.get_status()}
        return ticket
