import math
from math import ceil, floor, log

PRIMES_UPTO_1000 = {
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
    283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
    353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
    419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
    467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
    547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
    607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
    661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
    739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
    811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
    877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
    947, 953, 967, 971, 977, 983, 991, 997
}

def log2(x): return log(x, 2)

def prime_sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, limit + 1):
        if sieve[i]:
            yield i
            for j in range(i*i, limit + 1, i):
                sieve[j] = False

def int_root(x, y):
    """
    Computes the integer z s.t. x^(1/y) = z.
    Uses binary search.
    Returns -1 if not a power.
    """
    if x==0: return 0
    if x==1: return 1
    if y==1: return x
    if x<y: return -1 # not an int

    lo, hi = 1, 1 << ((x.bit_length() + y - 1) // y)
    while lo <= hi:
        mid = (lo + hi) // 2

        # compute mid^y with early exit
        val = 1
        for _ in range(y):
            val *= mid
            if val > x:
                break

        if val==x:
            return mid
        if val<x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1

def is_perfect_power(x):
    for b in prime_sieve(floor(log2(x))+1):
        if int_root(x, b) != -1: return True
    return False

def poly_mul_modQ(a, b, q, n):
    """
    Multiply polynomials a and b in Z_n[z]/(Q).
    a, b: lists of length d
    q:    coefficients of Q (length d)
    """
    d = len(q)
    tmp = [0] * (2*d - 1)

    # convolution
    for i in range(d):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(d):
            tmp[i + j] = (tmp[i + j] + ai * b[j]) % n

    # reduce degrees >= d using z^d = -(q[d-1]z^{d-1}+...+q[0])
    for k in range(2*d - 2, d - 1, -1):
        c = tmp[k]
        if c == 0:
            continue
        t = k - d
        for i in range(d):
            tmp[i + t] = (tmp[i + t] - c * q[i]) % n
        tmp[k] = 0

    return tmp[:d]

def poly_pow_modQ(base, exp, q, n):
    d = len(q)
    res = [0]*d
    res[0] = 1   # constant 1

    cur = base[:]
    e = exp
    while e > 0:
        if e & 1:
            res = poly_mul_modQ(res, cur, q, n)
        e >>= 1
        if e:
            cur = poly_mul_modQ(cur, cur, q, n)
    return res

def mersenne_reduce(a, p, M):
    """Return a mod (2^p-1) using folding reduction (fast, division-free)."""
    # ensure non-negative
    if a < 0:
        a %= M
        return a

    # fold high bits down
    while a >> p:
        a = (a & M) + (a >> p)

    # now a < 2^p + something small; finish with at most a couple subtractions
    if a >= M:
        a -= M
        if a >= M:
            a -= M

    return a # in [0, M-1]

def mult_ord(a, n):
    """ord_n (a), or mult order of a mod n, = smallest pos int k s.t a^k = 1 (mod n)"""
    assert n > 1, "modulus must be larger than 1"
    if a % n == 1: return 1
    a_, k = a, 1
    while a_ % n != 1:
        k += 1
        a_ = a_ * a
    return k

def gcd(a, b):
    if a==0 or b==0: return 0
    if a==b: return a
    if a>b: return gcd(a-b, b)
    return gcd(a, b-a)

def are_coprime(a, b):
    return gcd(a, b) == 1

def euler_totient(x):
    return sum(are_coprime(x, k) for k in range(1, x+1))