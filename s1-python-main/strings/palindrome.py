# -*- coding: utf-8 -*-
"""
May 2019
Palindrome
"""

# authorized function: chr and ord


def lower(c):
    '''
    Return a copy of the character c converted to lowercase
    works only with non accented letters
    '''
    if (c < 'a') or (c > 'z'):
        return chr(ord(c) + 32)   #ord('a') - ord('A')
    else:
        return c


def free_accent(c):
    '''
    Return the letter c without accent (only with lowercase...)
    '''
    if c in ('é', 'è', 'ê', 'ë'):
        return 'e'
    elif c == 'à':
        return 'a'
    elif c in ('î', 'ï'):
        return 'i'
    elif c in ('ô', 'ö'):
        return 'o'
    elif c in ('ù', 'û'):
        return 'u'
    else:
        return c

#----------------------------------------------------------------------------
# first version: builds a new string
      
# reminder:
#      a string can be delimited by " ", or ' ', or ''' ''', or """ """
#      str values are unmutable

def remove_symbols(s):
    '''
    Return a copy of the string S without wymbols (only keeps letters)
    '''
    
    symbols = ''' !()-[]{};:'"\,<>./?@#$%^&*_~''' 
    sres = ""
    for c in s:
        if not c in symbols:
            sres = sres + lower(free_accent(c))
    return sres
    
    
def palindrome(s):
    s = remove_symbols(s)
    i = 0
    n = len(s)
    while (i < n // 2) and (s[i] == s[n-i-1]):
        i = i+1
    return i == n // 2

#----------------------------------------------------------------------------    
# second version
    
def palindrome2(s):
    symbols = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
    i = 0
    n = len(s) - 1
    is_pal = True
    while (i < n) and is_pal:
        while s[i] in symbols:
            i = i+1
        while s[n] in symbols:
            n = n-1
        if lower(free_accent(s[i])) != lower(free_accent(s[n])):
            is_pal = False
        else:
            i = i + 1
            n = n - 1
    return is_pal

def print_ascii(a, b):
    for i in range(a, b+1):
        print(chr(i))
