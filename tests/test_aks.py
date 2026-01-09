from aks import is_prime

def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(10) == False
    assert is_prime(31) == True
    assert is_prime(33) == False