# -*- coding: utf-8 -*-
"""
S1 - Tutorial 1 - Sequence
"""

def ligne(seq, nb, val):
    '''
    seq: integer representing the current sequence 
    nb: number of times val has been counted so far
    val: current value being counted
    returns the next line of the sequence from seq
    '''
    if seq == 0:
        return nb * 10 + val
    else:
        el = seq % 10
        if val == None :
            return ligne(seq//10, 1, el)
        elif el == val :
            return ligne(seq//10, nb+1, val)
        else:
            return (nb * 10 + val) + 100 * ligne(seq//10, 1, el)

def _sequence(n, seq) :
    '''
    n: order of the current sequence
    seq: integer representing the current sequence
    returns the nth line of the sequence from seq
    '''
    if n == 0:
        return seq
    else:
        return _sequence(n-1, ligne(seq, 0, None))

def sequence(n) :
    '''
    returns nth line of the sequence
    '''
    if n >= 0:
        return _sequence(n, 1)
