#!/usr/bin/python

# https://projecteuler.net/problem=7
# What is the 10,001st prime number?

from primes import generate

for n, prime in enumerate(generate()):
    if n == 10000:
        print prime
        break
