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

    lo, hi = 1, x
    while lo <= hi:
        mid = (lo + hi) // 2
        val = mid**y
        if val==x:
            return mid
        if val<x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1

def is_perfect_power(x):
    for b in range(2, floor(log2(x))+1):
        if b<=1000 and b not in PRIMES_UPTO_1000: continue
        if int_root(x, b) != -1: return True
    return False
