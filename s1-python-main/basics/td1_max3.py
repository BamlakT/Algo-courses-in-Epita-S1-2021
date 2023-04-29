# -*- coding: utf-8 -*-
"""
S1 - Tutorial 1 - maximum of 3 values
"""

# simple traduction (with correction)
def max3(x, y, z):
    '''
    returns the maximum between x, y and z
    '''
    if (x >= y) and (x >= z):
        m = x
    elif (y > z):
        m = y
    else:
        m = z
    return m

def max3(x, y, z):
    '''
    returns the maximum between x, y and z
    '''
    if x > y:
        if z > x:
            return z
        else:
            return x
    else:
        if z > y:
            return z
        else:
            return y
# or

def max3(x, y, z):
    '''
    returns the maximum between x, y and z
    '''
    if x > y:
        m = x
    else:
        m = y
    if z > m: 
        return z
    else:   
        return m


def max3Bis(x, y, z):
    '''
    returns the maximum between x, y and z
    '''
    if y > x:
        x = y
    if z > x:
        x = z
    return x

a = int(input("first number: "))
b = int(input("second number: "))
c = int(input("third number: "))

print("The maximum is:",max3Bis(a, b, c))
