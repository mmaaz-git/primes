def is_prime(x):
    """
    Tests if the number 2^x-1 is prime.
    """
    M = 2**x - 1
    s = 4
    for _ in range(x-2):
        s = (s**2 - 2) % M
    return s == 0