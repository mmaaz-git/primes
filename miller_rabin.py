import random

def is_prime(x, k=10):
    if x % 2 == 0: return False

    s, d = 0, x-1
    while d % 2 == 0:
        s += 1
        d = d // 2

    for _ in range(k):
        a = random.randint(2, x-2)
        y = a**d % x

        for _ in range(s):
            z = y*y % x
            if z==1 and y!=1 and y!=x-1: return False
            y = z

        if z!=1: return False

    return True
