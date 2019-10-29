from validations import *

'''
expense <day>(between 1 and 30),<money>(positive integer),<expense type>(housekeeping, food, transport, clothing, internet, others)
'''

def get_day(expense):
    return expense['day']
def get_money(expense):
    return expense['money']
def get_type(expense):
    return expense['type']

def set_day(expense,eday):
    expense['day'] = eday
def set_money(expense,emoney):
    expense['money'] = emoney
def set_type(expense,etype):
    expense['type'] = etype

def create_expense(eday, emoney, etype):
    '''
    Create an expense
    params:
        eday - the day (integer,1<=eday<=30)
        emoney - the amount of money (positive integer)
        etype - type of expense (housekeeping, food, transport, clothing, internet, others)
    raise an error if invalid data
    return the expense as a dictionary otherwise
    '''
    if not is_integer(eday):
        raise ValueError("not a valid day")
    if not is_integer(emoney):
        raise ValueError("not a valid amount of money")
    if not in_interval(eday,1,30):
        raise ValueError("not a valid day")
    if emoney < 0:
        raise ValueError("not a valid amount of money")
    if not in_expense_types(etype):
        raise ValueError("not a valid expense type")
    return {"day":eday, "money":emoney, "type":etype}


def init_expenses():
    '''
        Create an intial list of expenses
    '''
    expenses = []
    expenses.append(create_expense(10, 100, 'food'))
    expenses.append(create_expense(24, 10, 'others'))
    expenses.append(create_expense(10, 300, 'housekeeping'))
    expenses.append(create_expense(23, 50, 'internet'))
    expenses.append(create_expense(20, 20, 'transport'))
    expenses.append(create_expense(18, 350, 'clothing'))
    expenses.append(create_expense(12, 100, 'others'))
    expenses.append(create_expense(12, 17, 'food'))
    expenses.append(create_expense(12, 88, 'food'))
    expenses.append(create_expense(9, 10, 'transport'))
    expenses.append(create_expense(10, 200, 'clothing'))
    return expenses

def tostr(expense):
    return 'day: ' + str(get_day(expense)) + ', money: ' + str(get_money(expense)) + ' RON, expense type: ' + str(get_type(expense))