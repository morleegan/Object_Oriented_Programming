import uuid


class Show:
    """Show class: overarching class"""
    def __init__(self, seating_info=None, show_info=None):
        """Initialization of show, contains show info"""
        self.__wid = uuid.uuid4().hex
        self.__seating_info = seating_info
        self.__show_info = show_info

    def get_wid(self):
        return self.__wid

    def get_show_info(self):
        return self.__show_info

    def get_seating_info(self):
        return self.__seating_info

    def check_wid(self, wid):
        if self.__wid == wid:
            return True
        return False

    def search(self, key):
        pass

