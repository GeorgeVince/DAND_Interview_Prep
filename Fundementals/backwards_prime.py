# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:27:47 2017

@author: georg

Backwards Read Primes are primes that when read backwards in base 10 
(from right to left) are a different prime. (This rules out primes which 
are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes

13 is such because it's prime and read from right to left writes 31 which 
is prime too. Same for the others.
Task

Find all Backwards Read Primes between two positive given numbers 
(both inclusive), the second one being greater than the first one. The resulting 
array or the resulting string will be ordered following the natural order 
of the prime numbers.
Example

backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] 
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
"""

def isprime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


def backwardsPrime(start, stop):
    to_return = []
    for i in range(start, stop + 1):
        
        if isprime(i) and isprime(int(str(i)[::-1])):
            print (i)
            if str(i) != (str(i)[::-1]):
                to_return.append(i)
                
    
    return to_return
   

a = [9923, 9931, 9941, 9967]
print (backwardsPrime(1095047, 1095403))

print (isprime(1095403))
print (isprime(3045901))



