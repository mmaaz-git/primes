# trying to push the limits of the algorithms

import agrawal_biswas, lucas_lehmer
from time import time

for num in [
        31,
        61,
        89,
        107,
        127,
        521,
        607,
        1279,
        2203,
        2281,
        3217,
        4253,
        4423,
        9689,
        9941,
        11213,
        19937,
        21701,
        23209,
        44497,
        86243,
        110503
        132049,
        216091,
        756839,
        859433,
    ]:
    print(f"Testing if 2^{num}-1 is prime...")
    start = time()
    res = lucas_lehmer.is_prime(num)
    end = time()
    print(f"result: {res}")
    print(f"elapsed: {end-start:.2f} sec")
