# -*- coding: utf-8 -*-
"""
S1 Lists
part5: Problems
"""

#------------------------------------------------------------------------------
# ex 5.1

def get_even_odd(L):
    '''
    L: list
    returns (L1,L2) where
    L1 contains the elements in even positions in L
    L2 contains the elements in even positions in L
    '''
    i = 0
    l = len(L)
    L1 = []
    L2 = []
    while i < l-1:
        L1.append(L[i])
        L2.append(L[i+1])
        i = i+2
    if l%2 == 1:
        L1.append(L[l-1])
    return L1,L2
    
def get_sum(L):
    '''
    L: list
    returns the sum of all elements of L as a list
    '''
    res = [0]
    for i in range(len(L)):
        res [0] = res[0] + L[i]
        if res[0] > 9:
            ires = 0
            lr = len(res)-1
            while ires < lr and res[ires] > 9:
                res[ires] = res[ires] - 10
                res[ires+1] = res[ires+1] + 1
                ires = ires + 1
            if res[ires] > 9:
                res[ires] = res[ires] - 10
                res.append(1)
    return res
    
def __get_diff(L1, L2):
    '''
    L1: list
    L2: list
    returns the difference of the two integers L1 and L2
    as a list
    '''
    res = []
    retenue = 0
    l1,l2 = len(L1),len(L2)
    for i in range(l2-1):
        x = L1[i] - L2[i] - retenue
        if x<0:
            res.append(x+10)
            retenue = 1
        else:
            res.append(x)
            retenue = 0
    if l1>l2:
        x = L1[l2-1] - L2[l2-1] - retenue
        if x<0:
            res.append(x+10)
            retenue = 1
        else:
            res.append(x)
            retenue = 0
        for i in range(l2,l1-1):
            x = L1[i] - retenue
            if x<0:
                res.append(x+10)
                retenue = 1
            else:
                res.append(x)
                retenue = 0
        x = L1[l1-1] - retenue
        if x != 0:
            res.append(x)
            retenue = 0
    else:
        x = L1[l1-1] - L2[l1-1] - retenue
        if x<0:
            res.append(x+10)
            retenue = 1
        else:
            if x != 0:
                res.append(x)
                retenue = 0
    return res

#bonus    
def get_diff(L1, L2):
    '''
    L1: list
    L2: list
    returns the absolute value of the difference of the two integers L1 and L2
    as a list
    '''
    l1,l2 = len(L1),len(L2)
    if l1 < l2:
        return __get_diff(L2, L1)
    else:
        if l2 < l1:
            return __get_diff(L1, L2)
        else:
            i = l1-1
            while i >= 0 and L1[i] == L2[i]:
                i = i - 1
            if i < 0:
                return [0]
            else:
                if L1[i] > L2[i]:
                    return __get_diff(L1, L2)
                else:
                    return __get_diff(L2, L1)

def div11_sum(L):
    while len(L)>2:
        L1,L2 = get_even_odd(L)
        L1,L2 = get_sum(L1),get_sum(L2)
        L = get_diff(L1,L2)
    if len(L) == 2:
        return L[0] == L[1]
    else:
        return L[0] == 0

#------------------------------------------------------------------------------
# ex 5.2 Eratosthenes BONUS
    
import math

def eratosthenes(n):
    prime = new_list(n+1, True)
    for i in range(2, int(math.sqrt(n))+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    L = []
    for i in range(2, n+1):
        if prime[i]:
            L.append(i)
    return L    
