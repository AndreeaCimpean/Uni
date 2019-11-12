from functions import *
from domain import *
import copy

def read_command():
    command = input("your command: ")
    idx = command.find(" ")
    if idx == -1:
        return (command,[])
    cmd = command[:idx]
    params = command[idx+1:]
    params = params.split(" ")
    copyParams = copy.deepcopy(params)
    params.clear()
    for i in range(0, len(copyParams)):
        parameter = copyParams[i]
        if parameter[len(parameter)-1] == 'i':
            ids = parameter.find("+")
            if ids != -1:
                params.append(parameter[:ids])
            else:
                ids = parameter.find("-")
                if ids != -1:
                    params.append(parameter[:ids])
            params.append(parameter[ids:len(parameter)-1])
        else:
            params.append(parameter)
    return (cmd,params)


def show_all_numbers(complexList):
    for c in range(0,len(complexList)):
        print(str(c) + '. ' + to_str(complexList[c]))

def show_all_reals_between_positions(compleList,start,end):
    for i in range(start,end+1)):
        if get_imaginary_part(compleList[i]) == 0:
            print(to_str(compleList[i]))

def write_numbers(complexList,cmd,params):
    if len(params) not in [0,3,4]:
        raise ValueError("Not a valid command")
    if len(params) == 0:
        show_all_numbers(complexList)
    elif len(params) == 4:
        if not is_integer(params[0]) or not is_integer(params[2]) or params[1]!='to':
            raise ValueError("Not a valid command")
        show_all_reals_between_positions(complexList,int(params[0]),int(params[2]))

def start():
    complexList = init_list()
    commands = {"add":add_complex_number,"insert":add_complex_number,"list":write_numbers,"remove":remove_complex_number,"replace":remove_complex_number}
    while True:
        command = read_command()
        cmd = command[0]
        params = command[1]
        if cmd == "exit":
            return
        elif cmd in commands.keys():
            try:
                commands[cmd](complexList,cmd,params)
            except ValueError as ve:
                print(ve)     
        else:
            print("Not a valid command")
        
start()