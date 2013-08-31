#!/usr/bin/python

# Pythonic prime number generator
# Many Project Euler problems use prime numbers, so I wrote this
# to avoid repeating myself.

from itertools import count

def generate():
    yield 2
    primes = []
    for i in count(3, 2):   #infinite sequence starting at 3, stepping by 2
        isPrime = True
        for prime in primes:
            if i % prime == 0:
                isPrime = False
        if isPrime:
            primes.append(i)
            yield i
