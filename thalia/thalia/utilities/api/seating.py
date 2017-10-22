import requests

from thalia.utilities.api.api import API


class SeatingAPI(API):
    """Seating API: returns status or json"""
    def __init__(self, *args, **kws):
        API.__init__(self, req_url='/seating')

        for opt in []:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def req_seats_auto(self, sid):
        """auto requests seats with sid"""
        try:
            r = requests.get(self.url + self.req_url + '/' + str(sid))
            r.raise_for_status()
            return r.json()
        except requests.HTTPError:
            return 404

    def req_seats_specific(self, sid, list_cid):
        """takes a list of seats to request"""
        try:

            r = requests.get(self.req_url + self.req_url + '?show=' + str(sid) + '&seats=' + str(list_cid))
            r.raise_for_status()
            return r.json()
        except requests.HTTPError:
            return 404

    def req_view_all(self):
        """does not have this functionality"""
        return NotImplemented

