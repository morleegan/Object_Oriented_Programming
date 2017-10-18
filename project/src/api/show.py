import requests
from .ticket import Api


class ShowApi(Api):
    """Show Api def"""
    def __init__(self):
        """Initialize shows api"""
        Api.__init__(self)
        self.url = self.url + "show/"

    def req_create(self):
        """create a show"""
        return requests.request("POST", self.url)

    def req_update(self, wid):
        """update a show"""
        return requests.request("PUT", self.url + wid)

    def req_delete(self, wid):
        """delete a show"""
        return requests.request("DELETE", self.url + wid)

    def req_sections(self, wid):
        """show sections of show"""
        return requests.request("GET", self.url + wid + "/sections")

    def req_section_by_id(self, wid, sid):
        """show section by show id and section id"""
        return requests.request("GET", self.url + wid + "/sections/" + sid)

