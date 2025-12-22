import agrawal_biswas
from utils import mersenne_reduce
import gmpy2
from gmpy2 import mpz, square

def is_prime(x):
    """
    Tests if the number 2^x-1 is prime.
    Requires x to be prime. I don't check that for now, as I am just trying to reproduce known Mersenne primes.
    """
    M = (mpz(1) << x) - 1
    s = mpz(4)

    for _ in range(x - 2):
        s = square(s)
        s -= 2
        s %= M

    return s == 0