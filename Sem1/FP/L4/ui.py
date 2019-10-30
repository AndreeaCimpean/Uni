
from functions import *
from domain import *
from tests import *
from validations import is_integer,in_expense_types,in_interval,validate_day

def help(expenseList,cmd,params,history):
    print("list - to show all expenses")
    print("list <type> - to show all expenses of a certain type")
    print("list <type> <[< / > / = ]> - to show all expenses of a certain type and a certain value")
    print("add <sum> <category> - to add to the current day an expense")
    print("insert <day> <sum> <category> - to add an expense")
    print("remove <day> - to remove expenses from a certain day")
    print("remove <start day> to <end day> - to remove expenses from a certain period")
    print("remove <type> - to remove expenses of a certain type")
    print("sum <category> - to show the total expense from a certain expense type")
    print("max day/<day> - to show the day with maximum expenses/to show the maximum expense for a certain day")
    print("sort day - to show the total daily expenses in scending order by amount of money spent")
    print("sort <category> - to show the daily expenses for a certain expense type in ascending order of money spent")
    print("filter <category> to keep only the expenses from a certain category")
    print("filter <type> <[< / > / = ]> - to keep only the expenses of a certain type and a certain value")
    print("exit - to exit de program")

def read_command():
    '''
    Read user's command
    no params
    output - the command and parameters as a tuple
    '''
    cmd = input("your command: ")
    idx = cmd.find(" ")
    if idx == -1:
        return (cmd,[])
    command = cmd[:idx]
    params = cmd[idx+1:]
    params = params.split(" ")
    for i in range(len(params)):
        params[i] = params[i].strip()
    return (command,params)

def get_entire_list(expenseList):
    '''
    Show entire list
    params:
        expenseList - the list of expenses
    print the list
    '''
    for e in expenseList:
        print(tostr(e))

def get_list_for_category(expenseList,category):
    '''
    Show list of expenses from a specified category
    params:
        expenseList - the list of expenses
        category - the expense type
    print the list
    '''
    for e in expenseList:
        if get_type(e) == category:
            print(tostr(e))

def get_list_money_grater(expenseList,category,value):
    '''
    Show list of expenses from a specified category with amount of money grater than a value
    params:
        expenseList - the list of expenses
        category - the expense type
        value - the value
    print the list
    '''
    for e in expenseList:
        if get_type(e) == category and get_money(e) > value:
            print(tostr(e))

def get_list_money_less(expenseList,category,value):
    '''
    Show list of expenses from a specified category with amount of money less than a value
    params:
        expenseList - the list of expenses
        category - the expense type
        value - the value
    print the list
    '''
    for e in expenseList:
        if get_type(e) == category and get_money(e) < value:
            print(tostr(e))

def get_list_money_equal(expenseList,category,value):
    '''
    Show list of expenses from a specified category with amount of money equal to a value
    params:
        expenseList - the list of expenses
        category - the expense type
        value - the value
    print the list
    '''
    for e in expenseList:
        if get_type(e) == category and get_money(e) == value:
            print(tostr(e))

def get_list(expenseList,cmd,params,history):
    '''
    Write the list of all expenses/all expense of a type/all expenses of a type with certain values
    params:
        expenseList - the list of expenses
        cmd - the command (list)
        params - the parameters of the wished type of list
        (history)
    if valid input data - call the suitable function for the wished list
    raise an error otherwise
    '''
    if len(params) == 0:
        get_entire_list(expenseList)
    elif len(params) == 1:
        if not in_expense_types(params[0]):
            raise ValueError("Not a valid command")
        else:
            get_list_for_category(expenseList,params[0])
            
    elif len(params) == 3:
        if not in_expense_types(params[0]) or not is_integer(params[2]):
            raise ValueError("Not a valid command")
        value = int(params[2])
        if params [1] == '>':
            get_list_money_grater(expenseList,params[0],value)
        elif params [1] == '<':
            get_list_money_less(expenseList,params[0],value)
        elif params [1] == '=':
            get_list_money_equal(expenseList,params[0],value)
        else:
            raise ValueError("Not a valid command")
    else:
        raise ValueError("Not a valid command")

def sum(expenseList,cmd,params,history):
    '''
    Print the sum of the expenses in a specific category if valid input
    params:
        expenseList - the list of expenses
        cmd - the command ('sum')
        params - the parameters given by the user
        (history)
    print the sum if valid input data
    raise an error otherwise
    '''
    if len(params) != 1:
        raise ValueError("Not a valid command")
    if not in_expense_types(params[0]):
        raise ValueError("Not a valid command")
    
    print('The total amount of money spent on ' + params[0] + ' is: ' + str(sum_on_category(expenseList,params[0])) + ' RON')

def max_expense(expenseList,cmd,params,history):
    '''
    Print the day with maximum expenses/print the maximum expense of a certain day depending on the parameters given by the user
    params:
        expenseList - the list of expenses
        cmd - the command('max')
        params - the parameters of the command given by the user
        (history)
    print the result if valid input data
    raise an error otherwise
    '''
    if len(params) != 1:
        raise ValueError("Not a valid command")
    if not is_integer(params[0]) and params[0] != 'day':
        raise ValueError("Not a valid command")
    if params[0] == 'day':
        result = day_with_max_expenses(expenseList)
        print('The day with maximum expenses is day: ' + str(result[0]) + ', ' + str(result[1]) + ' RON')
    else:
        if not validate_day(int(params[0])):
            raise ValueError("Not a valid command")
        expense = max_expense_on_day(expenseList,int(params[0]))
        if expense == {}:
            raise ValueError("No expenses in the specified day")
        else:
            print('The maximum expense from day ' + params[0] + ' is: ' + str(get_money(expense)) + ' RON on ' + get_type(expense))

def sort_days_ui(expenseList,cmd,params,history):
    '''
    Sort daily expenses in a category/the total daily expenses depending on user input
    params:
        expenseList - the list of expenses
        cmd - the command('sort')
        params - the parameters of the command given by the user ('day'/<category>)
    print the daily expenses sorted if valid input data
    raise an error otherwise
    '''
    if len(params) != 1:
        raise ValueError("Not a valid command")
    if params[0] != 'day' and not in_expense_types(params[0]):
        raise ValueError("Not a valid command")
    if params[0] == 'day':
        lst = sort_days(expenseList)
        for e in range(0,32):
            if lst[e][0] != 0:
                print("Day: " + str(lst[e][1]) + ", total expenses: " + str(lst[e][0]) + " RON")
    else:
        lst = sort_days_in_category(expenseList,params[0])
        for e in range(0,32):
            if lst[e][0] != 0:
                print("Day: " + str(lst[e][1]) + ", expenses: " + str(lst[e][0]) + " RON")

def filter_expenses(expenseList,cmd,params,history):
    ''' 
    Filter the list of expenses by category/by category and value depending on user input, update history
    params:
        expenseList - the list of expenses
        cmd - the command ('filter')
        params - the parameters of the command given by the user(<type>/<type> [</>/=] <value>)
        history - for doing undo
    print the filterd list if valid input data 
    raise an error otherwise
    '''
    if len(params) not in [1,3]:
        raise ValueError("Not a valid command")
    if not in_expense_types(params[0]):
        raise ValueError("Not a valid command")
    if len(params) == 1:
        history.append(expenseList.copy())
        filter_by_category(expenseList,params[0])
        get_entire_list(expenseList)
    else:
        if params[1] not in ['>','<','='] or not is_integer(params[2]):
            raise ValueError("Not a valid command")
        if params[1] == '>':
            history.append(expenseList.copy())
            filter_by_category_value_grater(expenseList,params[0],int(params[2]))
            get_entire_list(expenseList)
        elif params[1] == '<':
            history.append(expenseList.copy())
            filter_by_category_value_less(expenseList,params[0],int(params[2]))
            get_entire_list(expenseList)
        else:
            history.append(expenseList.copy())
            filter_by_category_value_equal(expenseList,params[0],int(params[2]))
            get_entire_list(expenseList)

def start():
    expenseList = init_expenses()
    history = []
    commandsList = {"add":add_expense,"insert":add_expense,"remove":remove_expenses,"list":get_list,"help":help,"sum":sum,"filter":filter_expenses,"undo":undo,"max":max_expense,"sort":sort_days_ui}
    while True:
        command = read_command()
        cmd = command[0]
        params = command[1]
        if cmd == 'exit':
            return
        if cmd in commandsList.keys():
            try:
                commandsList[cmd](expenseList,cmd,params,history)
            except ValueError as ve:
                print(ve)
        else:
            print("Not a valid command")

def call_tests():
    test_create_expense()
    test_add_expense_current_day()
    test_add_expense_certain_day()
    test_add_expense()
    test_remove_expense_between_two_days()
    test_remove_expense_from_category()
    test_remove_expense_from_day()
    test_remove_expense()
    test_tostr()

call_tests()
start()
