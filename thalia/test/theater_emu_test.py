from thalia.emulator import TheaterEmulator

section_emu = TheaterEmulator()


def test_theater_emu_make_json():
    sections = section_emu.make_json()
    for s in sections:
        assert list(s.keys()) == ['sid', 'section_name']


def test_make_section_by_id():
    sections = section_emu.make_json()
    sid = sections[0]['sid']
    sec_by_id = section_emu.make_section_by_id(sid)
    assert list(sec_by_id.keys()) == ['sid', 'section_name', 'seating']
    assert section_emu.make_section_by_id(0) is None


def test_seats_aut_emu():
    assert section_emu.make_seats_request(1,1) == NotImplemented


if __name__ == '__main__':
    test_seats_aut_emu()
    test_make_section_by_id()
    test_theater_emu_make_json()