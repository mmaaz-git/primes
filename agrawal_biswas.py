from utils import PRIMES_UPTO_1000, is_perfect_power, log2
from math import ceil, floor
import sympy as sp
import sympy.abc
from sympy.polys import Poly
from random import randint

def is_prime(x):
    PRIMES = [2,3,5,7,11,13]
    if x in PRIMES: return True
    if any(x % n == 0 for n in PRIMES): return False
    if is_perfect_power(x): return False

    # form the polynomial P(z) = (1+z)^x - 1 - z^x
    z = sp.abc.z
    P = (1+z)**x - 1 - z**x

    # now form the random polynomial Q(z)
    # it should be monic, degree ceil(log x) with coeffs in Z_x
    Q_deg = ceil(log2(x))
    Q = z**Q_deg + sum(z**n * randint(0,x) for n in range(Q_deg))

    # if P divides Q over Z_n then prime, else composite
    rem = Poly(P,z).rem(Poly(Q,z))
    return all(c % x == 0 for c in rem.coeffs())





