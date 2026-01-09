from agrawal_biswas import is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(1009) == True
    assert is_prime(2**31-1) == True

    num = 104717*104723 # product of some primes
    res = [is_prime(num) for _ in range(100)]
    assert sum(r==False for r in res) / len(res) >= 2/3 # bound from paper
