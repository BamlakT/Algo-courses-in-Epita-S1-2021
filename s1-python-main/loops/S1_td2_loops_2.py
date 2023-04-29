# -*- coding: utf-8 -*-
"""
S1 - Tutorial 2 - Loops part 2
"""

#----------------------- ex 2.1 -----------------------------------------------

def div11(n):
    '''
    checks if n is divisible by 11
    '''
    if n <= 0:
        raise Exception("n has to be greater than 0")
    else:
        while n >= 100:
            n = (n//10) - (n%10)
        return (n%10) == (n//10)


#----------------------- ex 2.2 -----------------------------------------------

def gcd(a, b):
    '''
    returns the gcd of a and b non-zero naturals
    '''
    if (a <= 0) or (b <= 0):
        raise Exception("works only with non-zero naturals")
    else:
        r = a % b
        while r != 0:
            a = b           # a, b = b, a % b
            b = r
            r = a % b
        return b

#----------------------- ex 2.3 -----------------------------------------------

def mirror(n):
    '''
    returns the mirror of integer n
    '''
    if n < 0:
        raise Exception("n not a natural")
    else:
        mir = 0
        while n != 0:
            mir = mir * 10 + n % 10
            n = n // 10
        return mir

#----------------------- ex 2.4 -----------------------------------------------

def euclid(a, b):
    '''
    returns (q, r) : quotient and rest of the euclidian division
    '''
    if (a <= 0) or (b <= 0):
        raise Exception("works only with non-zero naturals")
    else:
        q = 0
        while a >= b:
            a = a - b
            q = q + 1
        return (q, a)

# can also be done by successive additions
    
#----------------------- ex 2.5 -----------------------------------------------

def greatestEven(limit):
    '''
    returns the greatest even number such that n! < limit
    '''
    n = 1
    fact = 1
    while fact < limit:
        n = n + 1
        fact = fact * n
    n = n - 1   # n before fact >= limit
    return n - n % 2 
    
def greatestEven2(limit):
    '''
    returns the greatest even number such that n! < limit
    '''
    n = 2
    fact = 2
    while fact < limit:
        fact = fact * (n+2) * (n+1)
        n = n + 2
    return n-2
        
#----------------------- ex 2.6 -----------------------------------------------

import math

def prime(n):
    '''
    checks if n is a prime number
    '''
    if n < 2:
        raise Exception("n has to be greater than 2")
    if n % 2 == 0:
        return n == 2
    else:
        d = 3
        sqrt = int(math.sqrt(n))
        while (d <= sqrt) and (n % d != 0):
            d = d + 2
        return d > sqrt
        
#----------------------- ex 2.7 -----------------------------------------------

#BONUS

def egypt(a, b):
    '''
    returns a * b with the egyptian method
    '''
    if b < 0:
        b = -b   # (a, b) = (-a, -b)
        a = -a
    p = 0
    while b != 0:
        if b % 2 == 1:
            p = p + a
        (a, b) = (a *2, b // 2)
    return p
