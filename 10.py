#!/usr/bin/python

# https://projecteuler.net/problem=10
# Find the sum of all the primes below two million.

from primes import generate

sum = 0L
n = 2000000

for prime in generate():
    if prime < n:
        sum += prime
    else:
        print sum
        break
