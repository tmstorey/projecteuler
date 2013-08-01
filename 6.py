#!/usr/bin/python

# https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

sum = 0L
sum_of_squares = 0L

for i in xrange(1,101):
    sum += i
    sum_of_squares += i*i
square_of_sum = sum ** 2
difference = square_of_sum - sum_of_squares
print sum, square_of_sum, sum_of_squares, difference
