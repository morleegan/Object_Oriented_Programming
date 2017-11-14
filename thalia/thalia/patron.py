
class Patron:
    """Patron class"""

    def __init__(self, name='John Doe', phone="", email="", billing_address="", cc_num ="", cc_exp=""):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__billing_address = billing_address
        self.__cc_number = cc_num
        self.__cc_exp_date = cc_exp

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_bill_adr(self):
        return self.__billing_address

    def get_cc_num(self):
        return self.__cc_number

    def get_cc_exp(self):
        return self.__cc_exp_date
