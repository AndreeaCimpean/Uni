from domain import *
from functions import *

def print_menu():
    print("1 to show all coffees")
    print("2 to add a new coffee")
    print("3 to show coffees sorted")
    print("4 to filter coffees")
    print("5 to delete coffees from a given country")
    print("x to exit")

def show_all_coffees(listCoffee):
    print(" ")
    for i in listCoffee:
        print(to_str(i))

def show_sorted(listCoffee):
    listc = sorted(listCoffee)
    for i in listc:
        print(to_str(i))

def start():
    listCoffee = init_list()
    while True:
        print(" ")
        print("MENU")
        print(" ")
        print_menu()
        command = input("> ")
        if command == "x":
            return
        elif command == "1":
            show_all_coffees(listCoffee)
        elif command == "2":
            name = input("name = ")
            country = input("country = ")
            try:
                price = float(input("price = "))
                coffee = create_coffee(name,country,price)
                add_coffee(listCoffee,coffee)
            except ValueError as ve:
                print(ve)
        elif command == "3":
            show_sorted(listCoffee)
        elif command == "4":
            country = input("country = ")
            price = input("price = ")
            if len(price) > 0 and len(country) > 0:
                listf = filter_coffees_country_price(listCoffee,country,float(price))
                if len(listf) == 0:
                    print("no such coffees")
                else: 
                    show_all_coffees(listf)
            elif len(country) == 0:
                listf = filter_coffees_price(listCoffee,float(price))
                if len(listf) == 0:
                    print("no such coffees")
                else: 
                    show_all_coffees(listf)
            elif len(price) == 0:
                listf = filter_coffees_country(listCoffee,country)
                if len(listf) == 0:
                    print("no such coffees")
                else: 
                    show_all_coffees(listf)
        elif command == "5":
            country = input("country = ")
            delete_coffees_country(listCoffee,country)
        else:
            print("invalid command")

start()