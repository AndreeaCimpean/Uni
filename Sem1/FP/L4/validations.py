import datetime
import calendar
def is_integer(stringValue):
    '''
    Check if a string has an integer form
    params:
        stringValue - the supposed integer
    output:
        True - is like an integer
        False - is just a string
    '''
    try:
        int(stringValue)
        return True
    except ValueError:
        return False

def in_interval(x,start,end):
    '''
    Check if a number is in an interval
    params:
        x - the number
        [start,end] - the interval
    output:
        True - x is in the interval
        False - otherwise
    '''
    return x >= start and x <= end

def validate_day(day):
    today = datetime.datetime.now()
    return day > 0 and day <= calendar.monthrange(today.year, today.month)[1]

def in_expense_types(x):
    '''
    Check if x is in the list of expense types
    '''
    return x in ['housekeeping', 'food', 'transport','clothing', 'internet', 'others']
