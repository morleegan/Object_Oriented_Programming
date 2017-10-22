import requests

from thalia.utilities.api.api import API


class SearchAPI(API):
    """Search API: """
    def __init__(self, *args, **kws):
        API.__init__(self, req_url='/search')

        for opt in []:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def req_search(self, topic, key):
        try:
            r = requests.get(self.url + self.req_url + '?topic=' + str(topic)
                             + '&key=' + str(key))
            r.raise_for_status()
            return r.json()
        except requests.HTTPError:
            return 404
