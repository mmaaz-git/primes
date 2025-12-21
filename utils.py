import math
from math import ceil, floor, log

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
        if int_root(x, b) != -1: return True
    return False
