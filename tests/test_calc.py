from main import calc_basic_load

def test_basic():
    assert calc_basic_load(10, 2) == 10*25 + 2*180
