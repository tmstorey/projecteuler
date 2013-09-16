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

def all_divisors(prime_factors):
    if prime_factors:
        prime, exponent = prime_factors[0]
        for i in range(exponent+1):
            for j in all_divisors(prime_factors[1:]):
                yield (prime ** i) * j
    else:
        yield 1

for triangle in triangles():
    prime_factors = []
    divisors = []
    
    for prime in generate():
        if triangle == 1:
            break
        exponent = 0
        while triangle % prime == 0:
            triangle /= prime
            exponent += 1
        if exponent:
            prime_factors.append((prime, exponent))
    
    for divisor in all_divisors(prime_factors):
        divisors.append(divisor)
    
    if len(divisors) > 500:
        print divisors[-1]
        break
