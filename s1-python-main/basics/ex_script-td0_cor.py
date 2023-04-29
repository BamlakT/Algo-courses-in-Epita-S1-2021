# -*- coding: utf-8 -*-
"""
S1 - Tutorial 1 - First example correction
@author: Nathalie
"""

def test(n):
    return (n >= 100) and (n < 1000)
    
def digits(n):
    """ 
        returns a tuple of the 3 digits of n (a 3-digit integer)
    """
    return (n // 100, (n // 10) % 10, n % 10)

def loop(n):
    if n >= 1000:
        return -1
    else:
        (a, b, c) = digits(n)
        if a + b + c == a * b * c:
            return n
        else:
            return loop(n + 1)

# main

print("Give a 3-digit integer")
n = int(input())
if test(n):
    res = loop(n)
    if res == -1:
        print("No mystery number after", n)
    else:
        print(res, "is the mystery number")
else:
    print(n, "is invalid")
