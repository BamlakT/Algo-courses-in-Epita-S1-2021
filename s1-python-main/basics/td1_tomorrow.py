# -*- coding: utf-8 -*-
"""
S1 - Tutorial 1 - Tomorrow
"""

def leap(year):
    '''
    year: integer representing the year
    returns True if year is a leap year, False otherwise
    '''
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def day_number(m, y):
    '''
    m: integer representing the month
    y: integer representing the year
    returns the number of days of the month m for the year y
    '''
    if m == 2:
        if leap(y):
            return 29
        else:
            return 28
    elif m in (4, 6, 9, 11):    
        # in is authorized only with small tuples (not with lists)
        return 30
    else:
        return 31

        
def valid(d, m, y):
    '''
    d: integer representing the day
    m: integer representing the month
    y: integer representing the year
    checks if the date given by d, m and y is valid.
    '''
    return (m > 0) and (m < 13) and (d > 0) and (d <= day_number(m,y))
    

def tomorrow_(d, m, y):
    '''
    prints the date (day, month, year) of the day after (d, m, y)
    '''
    if not valid(d, m, y):
        print("non-valid")
    else:
        d = d + 1
        if d > day_number(m, y):
            d = 1
            m = m + 1
            if m == 13:
                m = 1
                y = y + 1
        print("The day after:", d, '/', m, '/', y)

# another version
def tomorrow(d, m, y):
    '''
    prints the date (day, month, year) of the day after (d, m, y)
    '''
    if not valid(d, m, y):
        print("non-valid")
    else:
        d = d % day_number(m ,y) + 1
        if d == 1:
            m = m % 12 + 1
            if m == 1:
                y = y + 1
        print("The day after:", d, '/', m, '/', y)
