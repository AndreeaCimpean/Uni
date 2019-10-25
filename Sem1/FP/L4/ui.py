
from functions import *
from domain import *

def help(expenseList,cmd,params):
    print("list - to show all expenses")
    print("list <type> - to show all expenses of a certain type")
    print("list <type> <[< / > / = ]> - to show all expenses of a certain type and a certain value")
    print("add <sum> <category> - to add to the current day an expense")
    print("insert <day> <sum> <category> - to add an expense")
    print("remove <day> - to remove expenses from a certain day")
    print("remove <start day> to <end day> - to remove expenses from a certain period")
    print("remove <type> - to remove expenses of a certain type")
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
    for e in expenseList:
            print(tostr(e))

def get_list_for_category(expenseList,category):
    for e in expenseList:
        if get_type(e) == category:
            print(tostr(e))

def get_list_money_grater(expenseList,category,value):
    for e in expenseList:
        if get_type(e) == category and get_money(e) > value:
            print(tostr(e))

def get_list_money_less(expenseList,category,value):
    for e in expenseList:
        if get_type(e) == category and get_money(e) < value:
            print(tostr(e))

def get_list_money_equal(expenseList,category,value):
    for e in expenseList:
        if get_type(e) == category and get_money(e) == value:
            print(tostr(e))

def get_list(expenseList,cmd,params):
    '''
    Write the list of all expenses/all expense of a type/all expenses of a type with certain values
    params:
        expenseList - the list of expenses
        cmd - the command (list)
        params - the parameters of the wished type of list
    if valid input data - call the suitable function for the wished list
    raise an error otherwise
    '''
    if len(params) == 0:
        get_entire_list(expenseList)
    elif len(params) == 1:
        if params[0] not in ['housekeeping', 'food', 'transport','clothing', 'internet', 'others']:
            raise ValueError("Not a valid command")
        else:
            get_list_for_category(expenseList,params[0])
            
    elif len(params) == 3:
        if params[0] not in ['housekeeping', 'food', 'transport','clothing', 'internet', 'others'] or not is_integer(params[2]):
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

def start():
    expenseList = init_expenses()
    commandsList = {"add":add_expense,"insert":add_expense,"remove":remove_expense,"list":get_list,"help":help}
    while True:
        command = read_command()
        cmd = command[0]
        params = command[1]
        if cmd == 'exit':
            return
        if cmd in commandsList.keys():
            try:
                commandsList[cmd](expenseList,cmd,params)
            except ValueError as ve:
                print(ve)
        else:
            print("bad command")

start()
