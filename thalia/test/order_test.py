from thalia.order import Orders


def test_create_order():
    order = Orders()
    assert isinstance(order, Orders)
