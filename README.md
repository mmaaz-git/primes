# Prime testing algorithms

A repository where I am experimenting with different primality tests

Currently implemented:
- Agrawal-Biswas (https://www.cse.iitk.ac.in/users/manindra/algebra/identity.pdf)
- Lucas-Lehmer, for prime testing of numbers of the form 2^n-1 (n prime)
- Miller-Rabin
- AKS

See `benchmarks.txt` for some benchmarking. I've checked `2^756839-1` (227,832 digits) is prime in 42.88 min with Lucas-Lehmer.
