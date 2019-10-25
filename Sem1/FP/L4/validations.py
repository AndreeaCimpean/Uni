def is_integer(stringValue):
    '''
    Check if a string has an integer form
    params:
        stringValue - the supposed number
    output:
        True - is a integer like
        False - is just a string
    '''
    try:
        int(stringValue)
        return True
    except ValueError:
        return False
