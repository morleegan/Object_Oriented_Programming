from thalia.tickets import Ticket


def test_create_ticket():
    ticket = Ticket()
    assert ticket is not None


if __name__ == '__main__':
    test_create_ticket()