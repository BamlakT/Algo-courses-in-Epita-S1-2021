# -*- coding: utf-8 -*-

''' 3 ways to traverse a string '''

def print_string(s):
    '''
    s: string
    displays the string s
    '''
    i = 0
    n = len(s)
    while i < n:
        print(s[i])
        i = i + 1

def print_string2(s):
    '''
    s: string
    displays the string s
    '''
    for i in range(len(s)):
        print(s[i], end='-')

def print_string3(s):
    '''
    s: string
    displays the string s
    '''
    for c in s:
        print(c, end='')

#----------------------- ex 1.1 -----------------------------------------------

def count(s, c):
    '''
    s: string
    c: character (represented by a string)
    returns the number of occurences of c in s
    '''
    i = 0
    n = len(s)
    cpt = 0
    while i < n:
        if s[i] == c:
            cpt = cpt + 1
        i = i + 1
    return cpt
    
def count2(s, c):
    '''
    s: string
    c: character (represented by a string)
    returns the number of occurences of c in s
    '''
    cpt = 0
    for i in range(len(s)): # range generates the whole sequence 
        if s[i] == c:       # at the beginning, so len will be called only once!
            cpt = cpt + 1
    return cpt
    
def count3(s, c):
    '''
    s: string
    c: character (represented by a string)
    returns the number of occurences of c in s
    '''
    cpt = 0
    for ch in s:
        if c == ch:
            cpt = cpt + 1
    return cpt

def in_string(s, c):
    '''
    s: string
    c: character (represented by a string)
    returns the first position of c in s
    -1 otherwise
    '''
    i = 0
    n = len(s)
    while (i < n) and (s[i] != c):
        i = i + 1
    if i < n:
        return i
    else:
        return -1

#Bonus
def substring(s, sub):
    '''
    s: string
    sub: string
    returns the first position of sub in s
    -1 otherwise
    '''
    nsub = len(sub)
    n = len(s) - nsub
    i = 0
    j = nsub - 1
    while i <= n and j < nsub:
        j = 0
        while j < nsub and sub[j] == s[i+j]:
            j = j + 1
        i = i + 1
    if j == nsub:
        return i-1
    else:
        return -1

#----------------------- ex 1.2 -----------------------------------------------
    
def div11_pal_str(s):
    '''    
    s: string representing an integer
    tests whether the number s is divisible by 11
    '''
    n = len(s)
    if n%2 == 1:
        return False
    else:
        i = 0
        while i < n//2 and s[i] == s[n-i-1]:
            i = i+1
        return i == n//2

#----------------------- ex 2.1 -----------------------------------------------

# power

def power(x, n):
    '''
    x: integer
    n: integer
    returns x^n only if n is a natural!
    '''
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return power(x*x, n//2)
        else:
            return power(x*x, n//2) * x
            
# decimal integer -> p-bit two’s complement representation
    
def dec_to_bin(n, p):
    '''
    n: integer
    p: integer
    returns the conversion of a decimal number n (>=0) 
    in binary representation in p bits as a string
    '''
    s = ""
    while n != 0:
        s = str(n % 2) + s
        n = n // 2
    while len(s) < p:
        s = '0' + s
    return s

# with power
def integer_to_twoscomp(n, p):
    '''
    n: integer
    p: integer
    returns the p-bits two's complement representation of the integer n
    '''
    if n < 0:
        n = power(2, p) + n
    return dec_to_bin(n, p)


def not_b(c):
    '''
    c: single character represented by a string
    returns the complement of the bit represented by c
    '''
    if c == '1':
        return '0'
    else:
        return '1'

# without power: use the method seen in the architecture lecture
def integer_to_twoscomp2(n, p):
    '''
    n: integer
    p: integer
    returns the p-bits two's complement representation of the integer n
    '''
    if n < 0:
        sign = -1
    else:
        sign = 1
    s = dec_to_bin(sign*n, p)
    if sign == -1:
        s2 = ""     # str unmutable
        i = p-1
        while s[i] != '1':      # True eventually
            s2 = s[i] + s2
            i = i - 1
        s2 = '1' + s2
        i = i - 1
        while i >= 0:
            s2 = not_b(s[i]) + s2
            i = i - 1
        s = s2
    return s
    
# p-bit two’s complement representation -> decimal integer
    
def bin_to_dec(s):
    '''
    s: string
    returns the conversion of a binary number s 
    represented by a string in decimal 
    '''
    n = 0
    for b in s:
        n = n * 2 + int(b)
    return n

# with power, the above method can also be used
def twoscomp_to_integer(b, p):
    '''
    b: string
    p: integer
    returns the conversion of a p-bits two's complement representation of 
    b into a decimal integer
    '''
    n = bin_to_dec(b)    
    if b[0] == '1':
        n = n - power(2, p)
    return n

def test(n, p):
    '''
    n: integer
    p: integer
    tests the validity of the functions 
    integer_to_twoscomp and twoscomp_to_integer
    '''
    return twoscomp_to_integer(integer_to_twoscomp(n,p), p) == n
    

#----------------------- ex 2.2 -----------------------------------------------

def frequent(s):
    '''
    s: string
    returns (nbmax, chmax):
    chmax: one of the most frequent char in s
    nbmax: number of chmax in s
    '''
    (nbmax, chmax) = (0, "")
    for i in range(len(s)):
        cpt = 0
        for j in range(i, len(s)):
            if s[i] == s[j]:
                cpt += 1
        if cpt > nbmax:
            (nbmax, chmax) = (cpt, s[i])
    return (nbmax, chmax)
    # this version is in n**2 (n(n+1)/2)

def frequent2(s):
    '''
    s: string
    returns (nbmax, chmax):
    chmax: one of the most frequent char in s
    nbmax: number of chmax in s
    '''
    (nbmax, chmax) = (0, "")
    for i in range(256):
        cpt = 0
        ch_i = chr(i)
        for c in s:
            if c == ch_i:
                cpt += 1
        if cpt > nbmax:
            (nbmax, chmax) = (cpt, ch_i)
    return (nbmax, chmax)
    # this version: 256 * n
    
# a better version later (with an histogram)

def nb_diff(s):
    '''
    s: string
    returns the number of different characters in s
    '''
    diff_char = ""
    for c in s:
        i = 0
        l = len(diff_char)
        while i < l and diff_char[i] != c:
            i = i + 1
        if i == l:
            diff_char = diff_char + c
    return len(diff_char)


from random import randint
def build_ex(n):
    '''
    n: integer
    returns a randomly built string of size n
    '''
    s = ""
    for i in range(n):
        s += chr(randint(0,255))
    return s
