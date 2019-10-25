from domain import *
from functions import *

'''
Module for tests
'''

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