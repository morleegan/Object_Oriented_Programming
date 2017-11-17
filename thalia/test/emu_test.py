from thalia.emulator import Emulator


def test_creation_emu():
    """Emulator Super class test"""
    emu = Emulator()
    assert emu.make_json() == NotImplemented
    assert emu.make_object() == NotImplemented
    assert emu is not None


if __name__ == '__main__':
    test_creation_emu()
