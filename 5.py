#!/usr/bin/python

# https://projecteuler.net/problem=5
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

primes = [2,3,5,7,11,13,17,19]
factors = [0 for i in primes]
result = 1

for i in xrange(2,20):
    for j, prime in enumerate(primes):
        count = 0
        while i % prime == 0:
            i /= prime
            count += 1
        if count > factors[j]:
            factors[j] = count

for j, prime in enumerate(primes):
    result *= prime ** factors[j]
    print factors[j], prime, result

print result