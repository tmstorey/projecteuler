#!/usr/bin/python

# https://projecteuler.net/problem=3
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
from primes import generate
from copy import copy

n = 600851475143
original = copy(n)
n_sqrt = sqrt(n)
solution = []

print n_sqrt

for prime in generate():
    if prime > n_sqrt:
        break
    while(n % prime == 0):
        solution.append(prime)
        n = n/prime
        n_sqrt = sqrt(n)
        print n_sqrt

solution.append(n)
print solution

print "The largest prime factor of", original, "is", solution[-1]
