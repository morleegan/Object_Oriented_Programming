import datetime


class ShowInfo:
    """Show API"""
    def __init__(self, web=None, name=None, date=datetime.datetime(day=2, month=2, year=2017), time=datetime.time()):
        self.__web = web
        self.__name = name
        self.__date = date
        self.__time = time

    def get_name(self):
        return self.__name

    def get_web(self):
        return self.__web

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def set_name(self, name):
        self.__name = name

    def set_web(self, web):
        self.__web = web

    def set_date(self, date):
        self.__date = date

    def set_time(self, time):
        self.__time = time

    def update_showinfo(self, showinfo_dict):
        self.set_date(showinfo_dict['date'])
        self.set_name(showinfo_dict['name'])
        self.set_time(showinfo_dict['time'])
        self.set_web(showinfo_dict['web'])



