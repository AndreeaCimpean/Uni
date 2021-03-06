from domain import *
from functions import *

'''
specification
tests & test-driven development
exceptions
simple feature-driven development
undo ?
modular programming
'''

'''
Menu-driven circles programm
    - add a circle (radius > 0, (+,+) first quadrant)
    - delete circles with radius smaller than a given radius
    - show circles
    - undo?
    - exit
'''

'''
evrything that read from/writes to the user (=console)
Nb! the only module where input/output/print call functions that do that
'''

'''
function calls:
ui -> functions
ui -> domain
functions -> domain
'''

def add_circle_ui(circles,history):
    #additional validation for reading integeres
    x = int(input("x= "))
    y = int(input("y= "))
    r = int(input("r= "))
    add_circle(circles,history,x,y,r)

def show_circles_ui(circles,history):
    for c in circles:
        print(tostr(c))

def print_menu():
    print("1.Add circle")
    print("3.Show circles")
    print("4.Undo")
    print("0. Exit")

def start():
    #circles = []
    circles = test_init()
    history = []
    #command design pattern
    commands = {"1":add_circle_ui,"3":show_circles_ui,"4":undo}
    while True:
        print_menu()
        cmd = input("command: ")
        if cmd == '0':
            return
        if cmd in commands.keys():
            try:
                commands[cmd](circles,history)
                print(history)
            except ValueError as ve:
                print(ve)
        else:
            print("bad command or file name")
        
start()
