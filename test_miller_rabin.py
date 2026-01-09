from miller_rabin import is_prime

def test_is_prime():
    assert is_prime(2) == False
    assert is_prime(37) == True
    assert is_prime(7919) == True
    assert is_prime(7917) == False