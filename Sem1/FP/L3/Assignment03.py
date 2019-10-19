'''
expense <day>(between 1 and 30),<money>(positive integer),<expense type>(housekeeping, food, transport, clothing, internet, others)
functionalities:
    1. Add a new expense
    2. Modify expenses from the list
    3. Write the expenses having differnt properties
    4. Obtain different characteristics of sublists
    5. Filter the list of expenses
    6. Undo the last operation
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
    output:
        a message if invalid data
        the expense as a dictionary otherwise
    '''
    if eday < 1 or eday > 30:
        return "Not a valid day"
    elif emoney <= 0:
        return "Not a valid amount of money"
    elif etype not in ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']:
        return "Not a valid type of expense"
    else:
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

def read_command():
    '''
    Read user's command
    no params
    output - the command and parameters as a tuple
    '''
    cmd = input("command: ")
    idx = cmd.find(" ")
    if idx == -1:
        return (cmd,[])
    command = cmd[:idx]
    params = cmd[idx+1:]
    params = params.split(" ")
    return (command,params)

def print_menu():
    print("1. Add a new expense")

def add_expense(expenseList,params):
    pass

def start():
    expensesList = []
    while True:
        command = read_command()
        cmd = command[0]
        params = command[1]
        if cmd == 'add':
            add_expense(expensesList,params)
        elif cmd == 'exit':
            return
        else:
            print("Bad command")

start()