import requests


class Api:
    """API superclass, (should not be used as a real call)"""
    def __init__(self):
        self.url = "http://localhost:8080/thalia/"

    def req_view(self, aid):
        """request a api id"""
        return requests.get(self.url + str(aid))

    def req_view_all(self):
        """request all"""
        return requests.request('GET', self.url)


class TicketApi(Api):
    """Ticket API calls"""
    def __init__(self):
        Api.__init__(self)
        self.url = self.url + "tickets/"

    def req_update(self, tid):
        """place at ticket in system"""
        req = requests.request('PUT', self.url + tid)
        return req

    def req_delete(self, tid):
        """delete a ticket from system"""
        req = requests.request('DELETE', self.url + tid)
        return req
