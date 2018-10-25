"""A class for generating primes

Implements a class called PrimeGenerator that generates primes using the Sieve of Eratosthenes
algorithm.

As a script, prints out the first num_primes entered primes
"""


class PrimeGenerator:
    """PrimeGenerator docstring

    A PrimeGenerator generates and keeps track of a sequence of consecutive primes
    """

    def __init__(self, num_primes=0):
        """PrimeGenerator constructor initializes a PrimeGenerator with given number of primes

        Initializes the primes list and the base Sieve. If num_primes is a positive integer,
        generates num_primes primes.
        
        :param num_primes: the number of primes to generate
        """

        self.primes = []
        self.sieve = _Sieve()
        if num_primes > 0:
            self.generate(num_primes)

    def next(self):
        """Generates, returns, and appends to the primes list the next prime number

        Generates the next prime number from sieve. Updates the sieve to be a new sieve
        containing the next_prime as its factor and self.sieve as its source.

        :return: returns the next generated prime number
        """

        next_prime = self.sieve.next()
        self.sieve = _Sieve(next_prime, self.sieve)
        self.primes.append(next_prime)
        return next_prime

    def generate(self, num_primes):
        """Generates the next num_primes primes and returns them as a list

        :param num_primes: the number of primes to generate
        :return: a list of the generated primes
        """

        generated_primes = []

        for i in range(num_primes):
            next_prime = self.next()
            generated_primes.append(next_prime)

        return generated_primes

    def __str__(self):
        """Returns a String representation of the primes list"""
        return str(self.primes)


class _Sieve:
    """Sieve docstring

    A Sieve generates a prime number that is not divisible by its own factor or the factor of
    any of its source Sieves"""

    def __init__(self, factor=1, source=None):
        """Sieve constructor

        Given no arguments, constructs the base Sieve

        :param factor: the factor that self makes sure its generated numbers are not divisible by
        :param source: the Sieve that self uses to get its candidate primes
        """

        self.factor = factor
        self.source = source

    def next(self):
        """Returns the next prime number

        :return: the next prime number
        """

        if self.source is None:
            self.factor += 1
            return self.factor
        else:
            candidate = self.source.next()
            while candidate % self.factor is 0:
                candidate = self.source.next()

            return candidate


def generate_primes(num_primes):
    """Generates and returns a list of num_primes primes

    :param num_primes: the number of primes to generate
    :return: a list of generated primes
    """

    prime_generator = PrimeGenerator(num_primes)
    return prime_generator.primes


if __name__ == "__main__":
    """Prints out the first num_primes entered primes
    
    Exits prematurely if an integer is not passed as the first script argument
    """
    import sys

    num_primes = 0

    if len(sys.argv) != 2:
        print "Usage:", sys.argv[0], "num_primes"
        exit(1)
    else:
        num_primes = int(sys.argv[1])

    for prime in generate_primes(num_primes):
        print prime,
    print ""
