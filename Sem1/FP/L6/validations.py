def isLeapYear(year):
    '''
    Check if the given year is a leap year
    params:
        year - the given year
    output
        True - if year is leap
        False - if year is not leap
    '''
    return (int(year)%4 == 0 and int(year)%100 != 0) or year%400 == 0