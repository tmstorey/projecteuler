#!/usr/bin/python

# https://projecteuler.net/problem=8
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for b in range(499, 0, -1):
    for c in range(500, b, -1):
        a = 1000 - b - c
        if b < a:
            break
        if a**2 + b**2 == c**2:
            print a, b, c
            print a*b*c
