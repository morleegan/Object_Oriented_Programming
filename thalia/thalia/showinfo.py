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



