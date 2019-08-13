#!/usr/bin/env python

def isPrime(num):
    """Brute force check on whether the argument is a prime number.
    
    Check if the argument is a prime number i.e. has only two positive
    divisors, 1 and the number itself. If the number is not a prime
    number, return its other positive divisors.
    """

    # Check argument is an integer
    if isinstance(num, int) == 0:
        print('Please pass an integer argument when calling the function.')
        return
    
    # Check argument is greater than 1
    if num <= 1:
        print('Please provide an integer greater than 1.')
        return
    
    # Create list to capture other positive divisors
    divisors = []
    
    # Check if argument has positive divisors other than 1 and itself
    for val in range(2, num):
        if num % val == 0:
            divisors.append(val)
            
    # If there are no other positive divisors
    if len(divisors) == 0:
        print(f'{num} is a prime number.')
    else:
        print(f'{num} is not a prime number, it has the following additional positive divisors:')
        for div in divisors:
            print(div)

if __name__ == '__main__':
    
    num = int(input('Please provide integer: '))
    isPrime(num)