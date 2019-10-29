import datetime
from domain import *
from validations import is_integer,in_expense_types

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

def add_expense(expenseList,cmd,params,history):
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
        history.append(expenseList.copy())
        add_expense_current_day(expenseList,int(params[0]),params[1])
    elif cmd == 'insert':
        if len(params) != 3:
            raise ValueError("Not a valid command")
        if not is_integer(params[0]) or not is_integer(params[1]):
            raise ValueError("Not a valid command")
        history.append(expenseList.copy())
        add_expense_certain_day(expenseList,int(params[0]),int(params[1]),params[2])
    
def remove_expenses_between_two_days(expenseList,start_day,end_day):
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

def remove_expenses_from_category(expenseList,category):
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

def remove_expenses_from_day(expenseList,day):
    '''
    Remove expenses from a day
    params:
        expenseList - the list of expenses
        day - the specific day
    remove the expenses from the list
    '''
    copyList = expenseList.copy()
    expenseList.clear()
    for e in copyList:
        eday = get_day(e)
        if eday != day:
            expenseList.append(e)

def remove_expenses(expenseList,cmd,params,history):
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
        history.append(expenseList.copy())
        remove_expenses_between_two_days(expenseList,start_day,end_day)
    else:
        if in_expense_types(params[0]):
            history.append(expenseList.copy())
            remove_expenses_from_category(expenseList,params[0])
        elif is_integer(params[0]):
            history.append(expenseList.copy())
            remove_expenses_from_day(expenseList,int(params[0]))
        else:
            raise ValueError("Not a valid command")

def sum_on_category(expenseList, category):
    '''
    Compute the sum of expenses for a category
    params:
        expenseList - the list of expenses
        category - the category
    output:
        the sum
    '''
    s = 0
    for e in expenseList:
        if get_type(e) == category:
            s+=get_money(e)
    return s

def day_with_max_expenses(expenseList):
    '''
    Find the day with maximum expenses
    params:
        expenseList - the list of expenses
    output:
        the day with maximum expenses
    '''
    dmax = -1
    max_expenses = -1
    for e1 in range(0,len(expenseList)):
        expenses = get_money(expenseList[e1])
        for e2 in range (e1+1,len(expenseList)):
            if get_day(expenseList[e2]) == get_day(expenseList[e1]):
                expenses+=get_money(expenseList[e2])
        if max_expenses < expenses:
            max_expenses = expenses
            dmax = get_day(expenseList[e1])
    return (dmax,max_expenses)

def max_expense_on_day(expenseList,day):
    '''
    Find the maximum expense from a day
    params:
        expenseList - the list of expenses
        day - the specified day
    output:
        the maximum expense
    '''
    maxExpenseValue = 0
    maxExpense = {} 
    for e in expenseList:
        if get_day(e) == day:
            if get_money(e) > maxExpenseValue:
                maxExpenseValue = get_money(e)
                maxExpense = e
    return maxExpense 

def sort_days(expenseList):
    '''
    Sort the total daily expenses in ascending order by amount of money
    params:
        expenseList - the list of expenses
    output:
        the total daily expenses as a list of pairs(total day expenses,day)
    '''
    lst = []
    for e in range (0,31):
        lst.append([0,e])
    for e in expenseList:
        lst[get_day(e)][0] += get_money(e)
    lst.sort(key = lambda x: x[0])
    return lst

def sort_days_in_category(expenseList,category):
    '''
    Sort the daily expenses from a category in ascending order by amount of money
    params:
        expenseList - the list of expenses
        category - the expense type
    output:
        the sorted daily expenses as a list of pairs(total day expenses,day)
    '''
    lst = []
    for e in range (0,31):
        lst.append([0,e])
    for e in expenseList:
        if get_type(e) == category:
            lst[get_day(e)][0] += get_money(e)
    lst.sort(key = lambda x: x[0])
    return lst

def filter_by_category(expenseList, category):
    copyList = expenseList.copy()
    expenseList.clear()
    for e in copyList:
        if get_type(e) == category:
            expenseList.append(e)

def filter_by_category_value_less(expenseList, category, value):
    copyList = expenseList.copy()
    expenseList.clear()
    for e in copyList:
        if get_type(e) == category and get_money(e) < value:
            expenseList.append(e)

def filter_by_category_value_grater(expenseList, category, value):
    copyList = expenseList.copy()
    expenseList.clear()
    for e in copyList:
        if get_type(e) == category and get_money(e) > value:
            expenseList.append(e)

def filter_by_category_value_equal(expenseList, category, value):
    copyList = expenseList.copy()
    expenseList.clear()
    for e in copyList:
        if get_type(e) == category and get_money(e) == value:
            expenseList.append(e)

def undo(expenseList,cmd,params,history):
    if len(params) != 0:
        raise ValueError("Not a valid command")
    if len(history) == 0:
        raise ValueError("No more undos")
    expenseList.clear()
    expenseList.extend(history.pop())
