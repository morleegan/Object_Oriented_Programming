from thalia.venue import Theater

s = [
      {
        "sid": "123",
        "price": 600
      },
      {
        "sid": "124",
        "price": 75
      },
      {
        "sid": "125",
        "price": 60
      }
    ]

test_theater = Theater()


def test_make_seating():
    test_theater.create_seating(s)
    assert test_theater.get_seating() is not None


if __name__ == '__main__':
    test_make_seating()
