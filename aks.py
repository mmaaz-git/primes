from utils import is_perfect_power, mult_ord, log2, are_coprime, poly_pow_modQ, euler_totient
from math import floor, sqrt

def is_prime(x):
    if is_perfect_power(x): return False

    log2_x_sq = log2(x)**2
    r = 2
    while True:
        if not are_coprime(x, r):
            r += 1
            continue
        if mult_ord(x, r) > log2_x_sq:
            break
        r += 1
    if not are_coprime(x, r): return False

    for a in range(2, min(r, x-1)+1):
        if x % a == 0: return False

    if x <= r: return True

    for a in range(1, floor(sqrt(euler_totient(r)) * log2(x))+1):
        q = [(-1) % x] + [0]*(r-1) # Q(z) = z^r - 1
        base = [a, 1] + [0]*(r-2) # X + a

        lhs = poly_pow_modQ(base, x, q, x)

        # RHS = X^x + a ≡ X^{x mod r} + a
        rhs = [0]*r
        rhs[0] = a % x
        rhs[x % r] = 1

        if lhs != rhs: return False

    return True




