#!/usr/bin/python

# https://projecteuler.net/problem=1
# Find the sum of all the multiples of 3 or 5 below 1000.
# e.g. (3+6+9+...+999) + (5+10+15+...+995) - (15+30+45+...+990)
# = 3+999 + 6+996 + 9+993 + ... + 498+504 + 501 + etc
# = 1002  + 1002  + 1002  + ... +  1002   + 501 + etc
# = 501*333 + etc
# (333 is how many numbers divisible by 3 there are between 0 and 1000)
# similarly for 5 and 15

numbers = [3, 5]
max = 1000

def total_sum(factors, maximum):
    sum = 0
    for index, x in enumerate(factors):
        sum += sum_of_multiples(x, maximum)
        for y in factors[:index]:
            sum -= sum_of_multiples(x*y, maximum)
    return sum

def sum_of_multiples(lowest, maximum):
    highest = maximum - (maximum % lowest)
    if(highest == maximum):
        highest = maximum - lowest
    n = float(highest/lowest)/2
    answer = int(n * (highest+lowest))
    print lowest, highest, n, answer
    return answer

print total_sum(numbers, max)