import uuid


class Show:
    """Show class: overarching class"""
    def __init__(self, seating_info=None, show_info=None):
        """Initialization of show, contains show info"""
        self.__wid = uuid.uuid4().hex
        self.seating_info = seating_info
        self.show_info = show_info

    def get_wid(self):
        return self.__wid

    def check_id(self, wid):
        if self.__wid == wid:
            return True
        return False

    def search(self, key):
        pass

