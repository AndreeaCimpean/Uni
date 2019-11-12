from domain import *
from validations import *

def add_complex_at_end(complexList,real,imaginary):
    number = create_complex_number(real,imaginary)
    complexList.append(number)

def add_complex_certain_position(complexList,real,imaginary,position):
    copyList = complexList.copy()
    complexList.clear()
    number = create_complex_number(real,imaginary)
    for i in range(0,position):
        complexList.append(copyList[i])
    complexList.append(number)
    for i in range(position,len(copyList)):
        complexList.append(copyList[i])

def add_complex_number(complexList,cmd,params):
    if cmd == "add":
        if len(params) != 2:
            raise ValueError ("Not a valid command")
        if not is_integer(params[0]) or not is_integer(params[1]):
            raise ValueError ("Not a valid command")
        add_complex_at_end(complexList,int(params[0]),int(params[1]))
    else:
        if len(params) != 4:
            raise ValueError("Not a valid command")
        if not is_integer(params[0]) or not is_integer(params[1]) or params[2]!='at' or not is_integer(params[3]):
            raise ValueError("Not a valid command")
        add_complex_certain_position(complexList,int(params[0]),int(params[1]),int(params[3]))

def remove_complex_at_position(complexList,position):
    copyList = complexList.copy()
    complexList.clear()
    for i in range(0,position):
        complexList.append(copyList[i])
    for i in range(position+1,len(copyList)):
        complexList.append(copyList[i])

def remove_complex_between_positions(complexList,start,end):
    copyList = complexList.copy()
    complexList.clear()
    for i in range(0,start):
        complexList.append(copyList[i])
    for i in range(end+1,len(copyList)):
        complexList.append(copyList[i])

def replace_complex(complexList,number1,number2):
    copyList = complexList.copy()
    complexList.clear()
    for i in range(0,len(copyList)):
        if copyList[i] == number1:
            complexList.append(number2)
        else:
            complexList.append(copyList[i])

def remove_complex_number(complexList,cmd,params):
    if cmd == "remove":
        if len(params) not in [1,3]:
            raise ValueError("Not a valid command")
        if len(params) == 1:
            if not is_integer(params[0]):
                raise ValueError("Not a valid command")
            remove_complex_at_position(complexList,int(params[0]))
        if len(params) == 3:
            if not is_integer(params[0]) or not is_integer(params[2]) or params[1] != 'to':
                raise ValueError("Not a valid command")
            remove_complex_between_positions(complexList,int(params[0]),int(params[2]))
    else:
        if len(params) !=5:
            raise ValueError("Not a valid command")
        if not is_integer(params[0]) or not is_integer(params[1]) or not is_integer(params[3]) or not is_integer(params[4]) or params[2]!='with':
            raise ValueError("Not a valid command")
        number1 = create_complex_number(int(params[0]),int(params[1]))
        number2 = create_complex_number(int(params[3]),int(params[4]))
        replace_complex(complexList,number1,number2)