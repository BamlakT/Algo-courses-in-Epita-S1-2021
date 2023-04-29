"""
S1 Lists
part2: Construction
"""

#------------------------------------------------------------------------------
# ex 2.1

def new_list(n, val):
    '''
    build a list with n values val
    '''
    L = []
    for i in range(n):
        L.append(val)
    return L
    
#------------------------------------------------------------------------------
# ex 2.2

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
    
#------------------------------------------------------------------------------
# ex 2.3

def get_sum(L):
    '''
    L: list
    returns the sum of all elements of L as a list
    '''
    sm = 0
    for el in L:
        sm = sm + el
    res = []
    while sm != 0:
        res.append(s%10)
        s = s // 10
    return res

#version with no conversion
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
