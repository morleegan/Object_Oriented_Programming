import requests

from thalia.utilities.api.api import API


class ReportAPI(API):
    """Reporting API"""
    def __init__(self, *args, **kws):
        """initialization"""
        API.__init__(self, req_url='/reports')
        for opt in []:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def req_view_by_date(self, start_date, end_date):
        """returns reports between start and end date"""
        try:
            r = requests.get(self.url + self.req_url + '[?start_date=' + str(start_date)
                             + '&end_date=' + str(end_date) + ']')
            r.raise_for_status()
            return r.json()
        except requests.HTTPError:
            return 404

    # past here are implemented by the API but are not used for reports (could be implemented later)
    def req_create(self, json_data):
        return NotImplemented

    def req_delete(self, rid):
        return NotImplemented

    def req_update(self, rid, json_data):
        return NotImplemented


