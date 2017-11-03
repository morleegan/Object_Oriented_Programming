
from thalia.show import Show
from thalia.section import Sections
from thalia.showinfo import ShowInfo


class Parser:
    """parses json recieved by GET and turns it into a class"""

    def __init__(self, **kwargs):
        self.keys = list()

        for opt in ['keys']:
            if opt in kwargs.keys():
                setattr(self, opt, kwargs[opt])

    def parse_json(self, js):
        pass

    def matches_keys(self, js):
        if self.keys == list(js.keys()):
            return True
        return False


class OrdersParser(Parser):
    """parses json into ShowInfo Object"""
    def __init__(self, **kws):
        Parser.__init__(self, **kws)


class ShowParser(Parser):
    """parses json to the Show Object"""
    def __init__(self, **kws):
        Parser.__init__(self, keys=['seating_info', 'show_info'])

    def parse_json(self, js):
        """Put call parsing function for shows"""
        new_seating_info = SeatingInfoParser(js=js['seating_info'])
        new_show_info = ShowInfoParser.parse_json(js=js['show_info'])
        new_show = Show(seating_info=new_seating_info, show_info=new_show_info)

        return {"wid": new_show.wid}

##############


class SeatingInfoParser:
    """since it is not called by the api we do not call to super class"""
    def __init__(self, **kwargs):
        pass

    @staticmethod
    def parse_json(js):
        return Sections(name=js['name'], price=['price'], row=RowParser())


class RowParser:
    def __init__(self):
        pass

    @staticmethod
    def parse_json(js):
        return js


class ShowInfoParser:
    def __init__(self):
        pass

    @staticmethod
    def parse_json(js):
        return js


def call_parser(given_json):
    """iterates through parsing types, returns parsed json, aka objects"""
    parser_opt = [Parser(), OrdersParser(), ShowParser()]
    for parser in parser_opt:
        if parser.matches_keys(js=given_json):
            return parser.parse_json(given_json)


if __name__ == '__main__':
    json = {"wid": 1}
    call_parser(json)
