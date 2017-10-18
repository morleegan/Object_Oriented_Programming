class Theater:
    """writen in through a "text/file will fill in requirements that way"""
    def __init__(self):
        # initialize Theater
        self.section = []
        self.section_price = dict()     # "main": 60
        self.section_tickets = dict()   # "main": [ticket1, ticket2,..]

    def get_tickets(self, key, numofseats):
        """key is section name"""
        ticket_sold = []
        for ticket in self.section_tickets[key]:
            if len(ticket_sold) == 0:
                ticket_sold.append(ticket)
            if ticket.seat > ticket_sold[len(ticket_sold)].seat:
                ticket_sold.append(ticket)
            if numofseats == len(ticket_sold):
                return ticket_sold
            else:
                ticket_sold = []



