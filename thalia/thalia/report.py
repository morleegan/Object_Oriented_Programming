from uuid import uuid4


class TotalReport:
    """Report class that creates the report for all of them"""
    def __init__(self, reports=list()):
        self.__report_list = reports


class OccupancyTotal(TotalReport):
    def __init__(self, reports=list()):
        TotalReport.__init__(self, reports=reports)
        self.__total_shows = len(reports)
        self.__total_seats = sum(int(occ.get_occupancy()) for occ in reports)
        self.__sold_seats = sum(int(sold.get_num_sold()) for sold in reports)


class SingleReport:
    """Report Class Abstract: used to create reports for a show"""
    def __init__(self, name='Report Name'):
        self.__name = name


class OccupancyReport(SingleReport):
    """Subclass of report class, just for occupancy reporting"""
    def __init__(self):
        SingleReport.__init__(self, name='Occupancy Report')
        self.__total_seats = 0
        self.__occupancy = 0
        self.__sold_seats = 0

    def get_sold_seats(self):
        return self.__sold_seats

    def get_occupancy(self):
        return self.__occupancy

    def get_total_seats(self):
        return self.__total_seats


class DonatedReport(SingleReport):
    """Subclass of the single report class, for the report about donations"""

