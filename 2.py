#!/usr/bin/python

# https://projecteuler.net/problem=2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# 1, 1, *2, 3, 5, *8, 13, 21, *34,
# even numbered is every third number (proof is left as excercise for the reader)

n = 4000000
a, b = 1, 1
sum = 0

while(b < n):
    b += a
    a = b - a
    if(b % 2 == 0):
        sum += b
print sum