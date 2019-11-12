def is_integer(number):
    try:
        int(number)
        return True
    except ValueError:
        return False