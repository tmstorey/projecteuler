#!/usr/bin/python

# https://projecteuler.net/problem=4
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
    forwards = str(n)
    backwards = forwards[::-1]
    return backwards == forwards

palindrome = 0

for i in xrange(999,99,-1):
    for j in xrange(999,i,-1):
        if isPalindrome(i*j) and i*j > palindrome:
            palindrome = i*j
            ij = (i,j)
            break

i, j = ij
print i, "*", j, "=", palindrome
