#!/usr/bin/python

# https://projecteuler.net/problem=14
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

current = [1,2,4]
checked = dict([(n, i) for i, n in enumerate(current)])
longest = current[-1]

for n in xrange(1000000, 499999, -1):
    current = []
    while n not in checked:
        current.append(n)
        if n % 2:
            n *= 3
            n += 1
        else:
            n /= 2
    length = checked[n]
    for num in current[::-1]:
        length += 1
        checked[num] = length
    if length > checked[longest]:
        longest = num
        
print longest
