from prime_generator import PrimeGenerator


def main():
    """Test program that uses the prime_generator module to print the first 500 prime numbers"""

    print "\nPrints out the first 500 prime numbers:\n"

    prime_generator = PrimeGenerator()
    for i in range(50):
        primes = prime_generator.generate(10)
        for j in range(10):
            print "{0:8d}".format(primes[j]),
        print


if __name__ == "__main__":
    main()