#!/usr/bin/python

# https://projecteuler.net/problem=3
# What is the largest prime factor of the number 600851475143 ?

import math

n = 600851475143
n_sqrt = math.sqrt(n)
primes = []
i = 1
solution = []

print n_sqrt
while(i <= n_sqrt):
    i += 1
    i_sqrt = math.sqrt(i)
    is_prime = True
    for p in primes:
        if p > i_sqrt:
            break
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
        while(not n % i):
            solution.append(i)
            n = n/i
            n_sqrt = math.sqrt(n)
            print n_sqrt
solution.append(n)
print solution