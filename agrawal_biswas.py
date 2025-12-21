from utils import PRIMES_UPTO_1000, is_perfect_power, log2, poly_pow_modQ, poly_mul_modQ
from math import ceil, floor
import sympy as sp
from sympy import ZZ
import sympy.abc
from sympy.polys import Poly
from random import randrange

def is_prime(x):
    if x in PRIMES_UPTO_1000: return True
    if any(x % n == 0 for n in PRIMES_UPTO_1000): return False
    if is_perfect_power(x): return False

    # form the random polynomial Q(z)
    # it should be monic, degree ceil(log x) with coeffs in Z_x
    deg = ceil(log2(x))
    Q = [1] + [randrange(x) for _ in range(deg-1)]

    # form polys for P(z)
    one = [0]*deg
    one[0] = 1

    z = [0]*deg
    if deg > 1:
        z[1] = 1

    base = one[:]
    if deg > 1:
        base[1] = 1   # 1 + z

    lhs = poly_pow_modQ(base, x, Q, x)
    rhs = one[:]
    zn  = poly_pow_modQ(z, x, Q, x)
    for i in range(deg):
        rhs[i] = (rhs[i] + zn[i]) % x

    return lhs==rhs





