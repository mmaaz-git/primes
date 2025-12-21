"""
This was my attempt at implementing the algorithm in
"DETECTING PERFECT POWERS IN ESSENTIALLY LINEAR TIME"
by Daniel J. Bernstein. I needed the algorithm that
checks if a number is a perfect power. It's somewhat
complicated, so for now I am just using a simpler one.
"""

from utils import log2
from math import ceil, floor

def extract_pow_two(x):
    """
    Computes n and a s.t. 2^a*n = x
    Returns tuple (n, a)
    """
    a = floor(log2(abs(x)))
    return x / 2**a, a

def approx_div(r, k, b):
    print(r,k,b)
    #if r==0: return 0

    # extract power of two
    n, a = extract_pow_two(r)

    # find f s.t. 2^{f-1} <= n < 2^f
    f = 0
    while not (2**(f-1) <= n < 2**f): f += 1
    #TODO: hangs here, probs better way!

    return 2**(a+f-ceil(log2(k))-b) * floor(n / 2**(f-ceil(log2(k))-b) * k)

def trunc(r, b):
    return approx_div(r, 1, b)

def approx_pow(r, k, b):
    if k==1: return trunc(r, b)
    elif k % 2 == 0:
        thepow = approx_pow(r, k/2, b)
        return trunc(thepow**2, b)
    else:
        thepow = approx_pow(r, k-1, b)
        return trunc(thepow * trunc(r, b), b)

def nroot_smallb(y, k, b):
    """
    Algorithm B in the paper.
    Only works for b <= 3 + ceil(log k)
    """
    assert 1 <= b <= 3 + ceil(log2(k)), "need b <= 3 + ceil(log k)"

    # find exponent g s.t. 2^{g-1} < y <= 2^g
    g = 0
    while not (2**(g-1) < y <= 2**g): g += 1

    a = floor(-g/k)
    B = ceil(log2(66*(2*k+1)))

    z = 2**a + 2**(a-1)
    j = 1

    while j != b:
        r = trunc(approx_pow(z, k, b) * trunc(y, b), b)
        if r <= 993/1024: z = z + 2**(a-j-1)
        elif r > 1: z = z - 2**(a-j-1)
        j = j + 1

    return z

def nroot_bigb(y, k, b):
    """
    Algorithm N in the paper.
    Only works for b >= 4 + ceil(log k)
    """
    assert b >= 4 + ceil(log2(k)), "need b >= 4 + ceil(log k)"

    b_ = ceil(log2(2*k)) + ceil((b - ceil(log2(2*k)))/2)
    B = 2*b_ + 4 - ceil(log2(k))

    if b_ <= ceil(log2(8*k)):
        z = nroot_smallb(y, k, b_)
    else:
        z = nroot_bigb(y, k, b_)

    r2 = trunc(z,B) * (k+1)
    r3 = trunc(approx_pow(z,k+1,B) * trunc(y,B), B)
    r4 = approx_div(r2-r3, k, B)

    return r4

print(nroot_smallb(50,10,5))

print(nroot_bigb(50,10,10))

def decompose_perfect_power(n):
    f = floor(log2(2*n, 2))
    y = nroot(n, 1, 3 + ceil(f/2))
    """
    Here, y=n, k=1, b=3+ceil(f/2)
    Now, consider: ceil(log k) = ceil(log 1) = 0
    For n=2, b=4, so in any case, b>=4.
    Hence, we are in the big-b regime.
    """