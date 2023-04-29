# -*- coding: utf-8 -*-
"""
S1 Lists
part3: A sense of Déjà Vu
"""

#------------------------------------------------------------------------------
# ex 3.1: 

def hist(s):
    '''
    s: string
    returns the histogram of characters in s
    i.e., returns a list (an array) of length 256 giving the number
    of occurrences of each character.
    '''
    h = newList(256, 0)
    for c in s:
        h[ord(c)] += 1
    return h

def nb_char(s):
    '''
    s: string
    returns the number of different characters occuring in the string s
    '''
    h = hist(s)
    nb = 0
    for n in h:
        if n > 0:         # nb = nb + (n != 0)
            nb = nb + 1
    return nb
    
def frequent3(s):
    '''
    s: string
    returns the most frequent character in the string s and its number of 
    occurrences
    '''
    h = hist(s)
    m = 0
    for i in range(1, 255):
        if h[i] > h[m]:
            m = i
    return h[m], chr(m)
    
#------------------------------------------------------------------------------
