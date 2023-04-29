# -*- coding: utf-8 -*-
"""
S1 Lists
part1: Basics
"""

#------------------------------------------------------------------------------
# ex 1.1: algorithms -> Python functions

def count(x, L):
    '''
    x: element
    L: list
    returns the number of occurrences of element x in L
    '''    
    cpt = 0
    for e in L:
        if e == x:         
            cpt = cpt + 1
    return cpt
    
def is_present(x, L):
    '''
    x: element
    L: list
    returns the first position of element x in L if it is present
    -1 otherwise
    '''
    i = 0
    n = len(L)
    while i < n and x != L[i]:
        i = i + 1
    return i < n

#------------------------------------------------------------------------------
# ex 1.2

# first versions: simple axiom traductions 
#    (k is the same as in axioms: the rank, not the position!)
    
def delete1(L, k):
    '''
    L: list
    k: index
    removes the element at position k in L
    '''
    # test preconditions
    if k < 1 or k > len(L):
        raise Exception("k out of range")
    
    #first axiom: the new list is of length: len(L) - 1
    R = new_list(len(L)-1, None)    # R is the result list
    
    #second axiom: first (k-1) values are the same as L's
    for i in range(k-1):
        R[i] = L[i]
    
    #third axiom: after k, each element at rank i in R is the one at rank i+1 in L
    for i in range(k-1, len(L)-1):
        R[i] = L[i+1]
    
    return R

def delete(L, k):
    '''
    L: list
    k: index
    removes the element at position k in L
    '''
    if k < 0 or k >= len(L):
        raise Exception("k out of range")
    for i in range(k, len(L)-1):  #shifts
        L[i] = L[i+1]
    L.pop() # to delete the unused last "cell"

#------------------------------------------------------------------------------
