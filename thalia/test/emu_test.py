from thalia.emulator import SectionsEmulator
from thalia.emulator import Emulator


def test_creation_emu():
    emu = Emulator()
    emu.make_json()
    assert emu is not None


def test_sections_emu():
    section_emu = SectionsEmulator()
    sections = section_emu.make_json()
    for s in sections:
        assert list(s.keys()) == ['sid', 'section_name']


def test_make_section_by_id():
    section_emu = SectionsEmulator()
    sections = section_emu.make_json()
    sid = sections[0]['sid']
    sec_by_id = section_emu.make_section_by_id(sid)
    assert list(sec_by_id.keys()) == ['sid', 'section_name', 'seating']


def test_seats_aut_emu():
    sectio_emu = SectionsEmulator()
    sections = sectio_emu.make_seats_request(1, 2, 3)
    assert sorted(list(sections.keys())) == sorted(['wid', 'sid', 'show_info', 'starting_seat_id', 'status',
                                                    'total_amount', 'seating', 'section_name'])


if __name__ == '__main__':
    test_sections_emu()
    test_make_section_by_id()
    test_seats_aut_emu()
    test_creation_emu()
