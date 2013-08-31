#!/usr/bin/python

import unittest
import argparse
import sys
import json
from itertools import imap
from operator import eq
from primes import generate

class TestPrimes(unittest.TestCase):
    """
    This requires the file '1048576primes.json' (8.3MB), which can be found at 
    http://archive.org/details/P1ThroughP1048576InJsonFormat
    """
    
    def setUp(self):
        print "Loading primes..."
        with open('1048576primes.json', 'r') as f:
            self.primes = json.load(f)
        if max:
            self.primes = self.primes[:max]
        print "Primes loaded."
    
    def test_primes(self):
        for x in imap(eq, self.primes, generate()):
            self.assertTrue(x)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()  # add an extra argument to test
    parser.add_argument(
        "-m", "--max", 
        type=int, 
        help="number of primes that will be tested")
    
    known, other = parser.parse_known_args()
    
    if known.max:
        max = known.max
    else:
        max=1000
    
    other = [sys.argv[0]] + other
    unittest.main(argv=other)   # pass the remaining args to unittest
