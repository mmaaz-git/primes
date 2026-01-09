from lucas_lehmer import is_prime

def test_is_prime():
    assert is_prime(31) == True
    assert is_prime(32) == False