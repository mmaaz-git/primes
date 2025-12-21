from utils import log2, int_root

def test_log2():
    assert log2(2) == 1
    assert log2(1024) == 10
    assert log2(3) <= 2

def test_int_root():
    assert int_root(4,2) == 2
    assert int_root(2,4) == -1
    assert int_root(27,3) == 3
    assert int_root(28,3) == -1
    assert int_root(0,5) == 0
    assert int_root(5,1) == 5