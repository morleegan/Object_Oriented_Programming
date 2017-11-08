import datetime
import uuid

# from thalia.utilities.connect import ApiCalls


class Show:
    """Show class: overarching class"""
    def __init__(self, **kws):
        """Initialization of show, contains show info"""
        # ApiCalls.__init__(self)
        self.wid = uuid.uuid4()
        self.seating_info = None
        self.show_info = None

        for opt in ['wid', 'seating_info', 'show_info']:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

    def check_id(self, wid):
        if self.wid == wid:
            return True
        return False

    def search(self, key):
        pass

