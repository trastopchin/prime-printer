# prime-printer
A program that prints out the first 500 prime numbers to the terminal.
Adapted from John David Stone's CSC-207 programming assignment "The
Sieve of Eratosthenes," from https://unity.homelinux.net/courses/object-oriented-programming/sieve-assignment.pdf\.

The prime_printer.py as a terminal script prints out the first 500
prime numbers to the terminal. These numbers are printed ten to a
row in fields 8 characters wide.


The prime_generator.py file defines functionality for generating
prime numbers. The PrimeGenerator class generates and keeps track
of a sequence of consecutive prime number. The _Sieve class is used
by the PrimeGenerator class in its implementation of the "sieve of
eratosthenes." The generate_primes function serves as a wrapper
function that simply instantiates a PrimeGenerator and generates
and returns a list of the specified number of primes. When used as
a terminal script, prime_generator.py expects the number of primes
as its argument and prints them to the terminal.