import requests
from .ticket import Api


class OrderApi(Api):
    """Order API class"""
    def __init__(self):
        Api.__init__(self)
        self.url = self.url + "orders/"

    def req_create(self):
        return requests.request("POST", self.url)

    def req_view_by_date(self, start, end):
        """get order from start date YYYYMMDD to end YYYYMMDD"""
        return requests.request("GET", self.url + '?start_date=' + start + "&end_date=" + end)

    def req_update(self, oid):
        """Update order"""
        return requests.request("PUT", self.url + oid)

