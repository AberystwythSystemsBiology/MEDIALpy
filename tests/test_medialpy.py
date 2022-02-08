import medialpy

def test_exists():
    assert medialpy.exists("T1DM")
    assert not medialpy.exists("JEDKH")