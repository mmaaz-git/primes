import agrawal_biswas
from utils import mersenne_reduce

def is_prime(x):
    """
    Tests if the number 2^x-1 is prime.
    Requires x to be prime. I don't check that for now, as I am just trying to reproduce known Mersenne primes.
    """
    M = 2**x - 1
    s = 4
    for _ in range(x-2):
        s = mersenne_reduce(s*s-2, x, M)
    return s == 0