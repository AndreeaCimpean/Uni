import datetime
from domain import *
from validations import is_integer

'''
functionalities:
    1. Add a new expense
    2. Modify expenses from the list
    3. Write the expenses having differnt properties
    4. Obtain different characteristics of sublists
    5. Filter the list of expenses
    6. Undo the last operation
'''


def add_expense_current_day(expenseList,emoney,etype):
    '''
    Add an expense for the current day
    params:
        expenseList - the list of expenses
        emoney - the amount of money
        etype - the type of the expense
    add expense for the current day
    '''
    today = datetime.datetime.now()
    eday = today.day
    expense = create_expense(eday,emoney,etype) 
    expenseList.append(expense)

def add_expense_certain_day(expenseList,eday,emoney,etype):
    '''
    Add an expense for a certain day
    params:
        expenseList - the list of expenses
        eday - the day of the expense
        emoney - the amount of money
        etype - the type of the expense
    add expense for the specified day
    '''
    expense = create_expense(eday,emoney,etype)
    expenseList.append(expense)

def add_expense(expenseList,cmd,params):
    '''
    Add an expense for the current day/for a certain day
    params:
        expenseList - the list of expenses
        cmd - the command (add/insert)
        params - the parameters of the expense 
    call the suitable add function depending on command if valid input data
    raise an error otherwise
    '''
    if cmd == 'add':
        if len(params) != 2:
            raise ValueError("Not a valid command")
        if not is_integer(params[0]):
            raise ValueError("Not a valid command")
        add_expense_current_day(expenseList,int(params[0]),params[1])
    elif cmd == 'insert':
        if len(params) != 3:
            raise ValueError("Not a valid command")
        if not is_integer(params[0]) or not is_integer(params[1]):
            raise ValueError("Not a valid command")
        add_expense_certain_day(expenseList,int(params[0]),int(params[1]),params[2])

def remove_expense_between_two_days(expenseList,start_day,end_day):
    '''
    Remove expenses between two days
    params:
        expenseList - the list of expenses
        start_day - the beginning day
        end-day - the end day
    remove the expenses from the list
    '''
    copyList = expenseList.copy()
    expenseList.clear()
    for e in copyList:
        eday = get_day(e)
        if eday < start_day or eday > end_day:
            expenseList.append(e)

def remove_expense_from_category(expenseList,category):
    '''
    Remove expenses from a category
    params:
        expenseList - the list of expenses
        category - the expense type
    remove the expenses from the list
    '''
    copyList = expenseList.copy()
    expenseList.clear()
    for e in copyList:
        if get_type(e) != category:
            expenseList.append(e)

def remove_expense_from_day(expenseList,day):
    '''
    Remove expenses from a day
    params:
        expenseList - the list of expenses
        day - the day
    remove the expenses from the list
    '''
    copyList = expenseList.copy()
    expenseList.clear()
    for e in copyList:
        eday = get_day(e)
        if eday != day:
            expenseList.append(e)

def remove_expense(expenseList,cmd,params):
    '''
    Remove expenses from a certain day/category / between two days
    params:
        expenseList - the list of expenses
        cmd - the command (remove)
        params - the parameters of the wished type of remove 
    if valid input data - calls the suitable remove function
    raise an error otherwise
    '''
    if len(params) not in [1,3]:
        raise ValueError("Not a valid command")
    if len(params) == 3:
        if not is_integer(params[0]) or not is_integer(params[2]):
            raise ValueError("Not a valid command")
        start_day = int(params[0])
        end_day = int(params[2])
        if start_day > end_day or params[1] != 'to' or start_day < 1 or start_day > 30 or  end_day < 1 or end_day > 30:
            raise ValueError("Not a valid command")
        remove_expense_between_two_days(expenseList,start_day,end_day)
    else:
        if params[0] in ['housekeeping', 'food', 'transport','clothing', 'internet', 'others']:
            remove_expense_from_category(expenseList,params[0])
        elif is_integer(params[0]):
            remove_expense_from_day(expenseList,int(params[0]))
        else:
            raise ValueError("Not a valid command")