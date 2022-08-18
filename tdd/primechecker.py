'''
   primechecker.py
   Jeff Ondich, 9 May 2012

   A small sample class to be tested by unittest-based test cases. See
   primetests.py for the rest of this sample.
'''

class PrimeChecker:
    def __init__(self, max_integer):
        self.max_integer = 0
        self.initialize_sieve(max_integer)

    def initialize_sieve(self, max_integer):
        ''' Initializes a Sieve of Eratothsenes up to but not including max_integer.
            Precondition: max_integer is an integer greater than 1. '''
        assert type(max_integer) == type(0)
        assert max_integer > 1
        if max_integer > self.max_integer:
            self.max_integer = max_integer
            self.sieve = [0] * self.max_integer
            self.sieve[0] = 1
            self.sieve[1] = 1
            current_prime = 2
            while current_prime < self.max_integer:
                k = current_prime * 2
                while k < self.max_integer:
                    self.sieve[k] = 1
                    k += current_prime
                current_prime += 1
                while current_prime < self.max_integer and self.sieve[current_prime] == 1:
                    current_prime += 1

    def get_max_integer(self):
        return self.max_integer

    def get_primes_below(self, n):
        ''' Returns the list of primes strictly less than n, sorted in increasing order. '''
        self.initialize_sieve(n)
        primes = [k for k in range(n) if self.sieve[k] == 0]
        return primes

    def is_prime(self, n):
        ''' Returns True if the specified integer is prime, and False otherwise.
            Preconditions: n is an integer between 1 and get_max_integer(), inclusive.
            Raises TypeError if n is not an integer, or ValueError if n is not
            in the proper range.
        '''
        if type(n) != type(0):
            raise TypeError('Parameter (type %s) must have type %s' % (str(type(n)), str(type(0))))

        if n < 1 or n > self.max_integer:
            raise ValueError('Integer parameter (%d) is out of range (1 to %d)' % (n, self.max_integer))

        assert self.max_integer == len(self.sieve)
        if n < 2:
            return False

        return self.sieve[n] == 0

