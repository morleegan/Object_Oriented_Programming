

class Theater:
    """im not sure i need this but i will leave it here... """
    def __init__(self, **kws):
        """Theater class initialization"""
        self.setup = None
        for opt in []:
            if opt in kws.keys():
                setattr(self, opt, kws[opt])

