# -*- coding: utf-8 -*-
"""
Frequencies: comparison different methods
"""
import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print(f.__name__, 'function tooks',(time2-time1)*1000.0,'ms')
        return ret
    return wrap


@timing
def frequent(s):
    '''
    s string assumed not empty
    returns (nbmax, c):
    chmax: the most frequent char in s
    nbmax: number of c in s
    '''
    nbmax = 0
    for i in range(len(s)):
        cpt = 0
        for j in range(i, len(s)):
            if s[i] == s[j]:
                cpt += 1
        if cpt > nbmax:
            (nbmax, chmax) = (cpt, s[i])
    return (nbmax, chmax)
    # this version is in n**2 (n(n+1)/2)

@timing
def frequent2(s):
    nbmax = 0
    for i in range(256):
        cpt = 0
        ch_i = chr(i)
        for c in s:
            if c == ch_i:
                cpt += 1
        if cpt > nbmax:
            (nbmax, chmax) = (cpt, ch_i)
    return (nbmax, chmax)
    
def histogram(s):
    '''
    returns the histogram of characters in s
    I.e., returns an array (type list) of length 256 giving the number
    of occurrences of each character.
    '''
    H = []
    for i in range(256):
        H.append(0)
    for c in s:
        H[ord(c)] += 1
    return H

@timing
def frequent3(s):
    H = histogram(s)
    m = 0
    for i in range(1, 256):
        if H[i] > H[m]:
            m = i
    return(H[m], chr(m))

def test(s):
    frequent(s)
    frequent2(s)
    frequent3(s)

'''
to build a string randomly
'''
from random import randint
def buildAleaStr(n):
    s = ""
    for i in range(n):
        s = s + chr(randint(0,256))
    return s

'''
result with a string of 50000 characters :
>>> test(s)
frequent function took 229260.82491874695 ms
frequent2 function took 1552.1481037139893 ms
frequent3 function took 15.62809944152832 ms
'''

def nbchars(s):
    """
    how many different characters in s
    """
    H = histogram(s)
    nb = 0
    for n in H:
        if n > 0:
            nb += 1
    return nb
    


