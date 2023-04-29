# -*- coding: utf-8 -*-
"""
S1 - Tutorial 1 - List to 9: displays the list AND returns its length
"""

# recursive version

def my_abs(n):
    '''
    n: integer
    returns the absolute value of the integer n
    '''
    if n < 0:
        return -n
    else:
        return n

def mirror(n):
    '''
    n: integer
    returns the mirror value of the positive two digit integer n
    '''
    return (10 * (n % 10) + n // 10)
    
def _list_to_9(n):
    '''
    n: integer
    prints the list to 9 from the positive two digit integer n
    '''
    print(n)
    if n == 9:
        return 1
    else:
        return 1 + _list_to_9(my_abs(n - mirror(n)))

def list_to_9(n):
    '''
    prints the list to 9 of n if n is a positive two digit integer
    '''
    if (n < 10) or (n >= 100):
        print(n, "is not a 2-digit positive integer")
        return 0
    elif n % 11 == 0:
        print("no list to 9!")
        return 0
    else:
        return _list_to_9(n)
