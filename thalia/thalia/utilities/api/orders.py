import requests

from thalia.utilities.api.api import API


class OrderAPI(API):
    """Order API"""
    def __init__(self, *args, **kws):
        API.__init__(self, req_url='/order')

        for opt in []:
            if opt in kws.keys:
                setattr(self, opt, kws[opt])

    def req_view_by_date(self, start_date, end_date):
        """returns orders in between the dates given"""
        try:
            r = requests.get(self.url + self.req_url + '?start_date=' + str(start_date)
                             + '&end_date=' + str(end_date))
            r.raise_for_status()
            return r.json()
        except requests.HTTPError:
            return 404
