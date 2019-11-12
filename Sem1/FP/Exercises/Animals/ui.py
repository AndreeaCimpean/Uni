from domain import *
from functions import *

def print_menu():
    print("1 to show all the animals")
    print("2 to add a new animal")
    print("3 to modify the type of an animal")
    print("4 to modify the type for a given species")
    print("5 to show all animals of a given type")
    print("x to exit")

def show_all_animals(listAnimals):
    for i in listAnimals:
        print(to_str(i))

def show_all_animals_given_type(listAnimals,atype):
    lista = []
    for i in listAnimals:
        if get_type(i) == atype:
            lista.append(i)
    listsorted = sort_by_name(lista)
    for i in listsorted:
        print(to_str(i))

def start():
    listAnimals = init_animals()
    while True:
        print(" ")
        print("MENU")
        print_menu()
        print(" ")
        command = input("> ")
        if command == "x":
            return
        elif command == "1":
            show_all_animals(listAnimals)
        elif command == "2":
            code = input("code = ")
            name = input("name = ")
            atype = input("type = ")
            species = input("species =")
            try:
                animal = create_animal(code,name,atype,species)
                add_animal(listAnimals,animal)
            except ValueError as ve:
                print(ve)
        elif command == "3":
            code = input("animal code = ")
            atype = input("new type = ")
            update_type_for_animal(listAnimals,code,atype)
        elif command == "4":
            species = input("species = ")
            atype = input("new type = ")
            try:
                update_type_for_species(listAnimals,species,atype)
            except ValueError as ve:
                print(ve)
        elif command == "5":
            atype = input("type = ")
            show_all_animals_given_type(listAnimals,atype)
        else:
            print("Invalid command")

start()