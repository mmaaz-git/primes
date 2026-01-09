from utils import log2, int_root, is_perfect_power, mult_ord

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

def test_is_perfect_power():
    assert is_perfect_power(27) == True
    assert is_perfect_power(28) == False
    assert is_perfect_power(37**53) == True
    assert is_perfect_power(37**53+1) == False

def test_mult_ord():
    assert ord(6, 5) == 1
    assert ord(5, 6) == 2
    assert ord(4, 7) == 3