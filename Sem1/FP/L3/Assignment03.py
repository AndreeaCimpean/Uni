import datetime

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
    if eday < 1 or eday > 30 :
        raise ValueError("not a valid day")
    if emoney < 0 or int(emoney) != emoney:
        raise ValueError("not a valid amount of money")
    if etype not in ['housekeeping', 'food', 'transport','clothing', 'internet', 'others']:
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

def tostr(expense):
    return 'day: ' + str(get_day(expense)) + ', money: ' + str(get_money(expense)) + ', expense type: ' + str(get_type(expense))
        
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

def test_create_expense():
    e = create_expense(2,100,'food')
    assert get_day(e) == 2 and get_money(e) == 100 and get_type(e) == 'food'

    # day not in the interval [1,30]
    try:
        e = create_expense(-1,10,'food')
        assert False
    except  ValueError:
        assert True

    # money not a positive integer
    try:
        e = create_expense(1,-10,'food')
        assert False
    except  ValueError:
        assert True

    try:
        e = create_expense(1,'abc','food')
        assert False
    except  ValueError:
        assert True

    # not a valid type    
    try:
        e = create_expense(1,10,'abc')
        assert False
    except  ValueError:
        assert True

def test_add_expense_current_day():
    today = datetime.datetime.now()
    eday = today.day
    elist = []
    add_expense_current_day(elist,30,'others')
    assert get_day(elist[0]) == eday and get_money(elist[0]) == 30 and get_type(elist[0]) == 'others'

    # money not a positive integer
    try:
        add_expense_current_day(elist,-1,'food')
        assert False
    except ValueError:
        assert True
    
    # not valid expense type
    try:
        add_expense_current_day(elist,10,'abcdef')
        assert False
    except ValueError:
        assert True

def test_add_expense_certain_day():
    elist = []
    add_expense_certain_day(elist,2,30,'others')
    assert get_day(elist[0]) == 2 and get_money(elist[0]) == 30 and get_type(elist[0]) == 'others'

    # money not a positive integer
    try:
        add_expense_certain_day(elist,1,-1,'food')
        assert False
    except ValueError:
        assert True

    # day not in [1,30]
    try:
        add_expense_certain_day(elist,100,1,'food')
        assert False
    except ValueError:
        assert True
    
    # not valid expense type
    try:
        add_expense_certain_day(elist,1,10,'abcdef')
        assert False
    except ValueError:
        assert True    


def test_add_expense():
    today = datetime.datetime.now()
    eday = today.day

    elist = []
    add_expense(elist,'insert',[2,30,'others'])
    assert get_day(elist[0]) == 2 and get_money(elist[0]) == 30 and get_type(elist[0]) == 'others'
    add_expense(elist,'add',[400,'housekeeping'])
    assert get_day(elist[1]) == eday and get_money(elist[1]) == 400 and get_type(elist[1]) == 'housekeeping'
    try:
        add_expense(elist,'add',[-1,'food'])
        assert False
    except ValueError:
        assert True
    
    try:
        add_expense(elist,'add',['food'])
        assert False
    except ValueError:
        assert True

    try:
        add_expense(elist,'insert',['clothing'])
        assert False
    except ValueError:
        assert True

def test_remove_expense_between_two_days():
    elist = []
    e1 = create_expense(10, 100, 'food')
    elist.append(e1)
    elist.append(create_expense(24, 10, 'others'))
    remove_expense_between_two_days(elist,11,25)
    assert len(elist) == 1 and elist[0] == e1


def test_remove_expense_from_category():
    elist = []
    e1 = create_expense(10, 100, 'food')
    elist.append(e1)
    elist.append(create_expense(24, 10, 'others'))
    remove_expense_from_category(elist,'others')
    assert len(elist) == 1 and elist[0] == e1

def test_remove_expense_from_day():
    elist = []
    e1 = create_expense(10, 100, 'food')
    elist.append(e1)
    elist.append(create_expense(24, 10, 'others'))
    remove_expense_from_day(elist,24)
    assert len(elist) == 1 and elist[0] == e1

def test_remove_expense():
    elist = []
    e1 = create_expense(10, 100, 'food')
    elist.append(e1)
    elist.append(create_expense(24, 10, 'others'))
    remove_expense(elist,'remove',['others'])
    assert len(elist) == 1 and elist[0] == e1

    # invalid input
    # invalid command
    try:
        remove_expense(elist,'remove',['abc'])
        assert False
    except ValueError:
        assert True

    # invalid command
    try:
        remove_expense(elist,'remove',[1,'food'])
        assert False
    except ValueError:
        assert True

    # start day > end day
    try:
        remove_expense(elist,'remove',[19,10])
        assert False
    except ValueError:
        assert True



def test_tostr():
    e = create_expense(1,1,'food')
    assert tostr(e) == 'day: 1, money: 1, expense type: food'
    e = create_expense(13,200,'clothing')
    assert tostr(e) == 'day: 13, money: 200, expense type: clothing'

test_create_expense()
test_add_expense_current_day()
test_add_expense_certain_day()
test_add_expense()
test_remove_expense_between_two_days()
test_remove_expense_from_category()
test_remove_expense_from_day()
test_remove_expense()
test_tostr()
start()