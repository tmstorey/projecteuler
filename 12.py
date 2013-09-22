#!/usr/bin/python

# https://projecteuler.net/problem=12
# What is the value of the first triangle number to have over
# five hundred divisors?

from primes import generate

def triangles():
    triangle = 0L
    i = 0L
    while True:
        i += 1
        triangle += i
        yield triangle

def num_divisors(exponents):
    product = 1
    for exponent in exponents:
        product *= exponent
    return product

for triangle in triangles():
    exponents = []
    divisors = []
    
    for prime in generate():
        if triangle == 1:
            break
        exponent = 0
        while triangle % prime == 0:
            triangle /= prime
            exponent += 1
        if exponent:
            exponents.append(exponent+1)
    
    if num_divisors(exponents) > 500:
        print divisors[-1]
        break
