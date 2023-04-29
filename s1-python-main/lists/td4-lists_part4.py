# -*- coding: utf-8 -*-
"""
S1 Lists
part4: Order
"""

#------------------------------------------------------------------------------
# ex 4.1

def search_sorted(L, x):
    '''
    L: list
    x: element
    returns the position of the first x found in the sorted list L
    -1 if x is not found
    '''
    i = 0
    l = len(L)
    while i < l and x > L[i]:
        i = i + 1
    if i < l and x == L[i]:
        return i
    else:
        return -1
        
#------------------------------------------------------------------------------
# ex 4.2

def search_indexes(L, val):
    '''
    L: list
    val: element
    returns the values of the first and last indexes of element val in the
    sorted list L
    (-1,-1) if val is not found
    '''
    i = 0
    l = len(L)
    while i < l and val > L[i]:
        i = i + 1
    if i < l and L[i] == val:
        start = i
        while i < l and val == L[i]:
            i = i + 1
        return start,i-1
    else:
        return -1,-1
        
#------------------------------------------------------------------------------
# ex 4.3

def insert(L, x):
    '''
    L: list
    x: element
    inserts element x in the strictly sorted list L
    returns True if the insertion occured
    False otherwise
    '''
    i = 0
    l = len(L)
    while i < l and x > L[i]:
        i = i + 1
    if i < l and x == L[i]:
        return False
    else:
        L.append(None)
        for k in range(l,i,-1):
            L[k] = L[k-1]
        L[i] = x
        return True

