from thalia.utilities.api.api import API


class TicketsAPI(API):
    """Ticket API:"""
    def __init__(self, *args, **kws):
        API.__init__(self, req_url='/tickets')

        for opt in []:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    # not asked to implement/ given as an option
    def req_create(self, json_data):
        return NotImplemented

