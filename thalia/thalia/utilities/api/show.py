import requests

from thalia.utilities.api.api import API


class ShowAPI(API):
    """Show API: defined in the documentation"""
    def __init__(self, *args, **kws):
        """initialize show api"""
        API.__init__(self, req_url='/shows')

        for opt in []:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def req_view_sections(self, rid):
        """request a sections of seats for a particular show"""
        try:
            r = requests.get(self.url + self.req_url + '/' + str(rid) + 'sections')
            r.raise_for_status()    # if 404 error
            return r.json()
        except requests.HTTPError:
            print('HTTPError: key error')
            return 404

