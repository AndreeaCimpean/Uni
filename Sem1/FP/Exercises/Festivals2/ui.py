from domain import *
from functions import *

def print_menu():
    print("1 to show all the festivals")
    print("2 to add a  new festival")
    print("3 to show all the festivals in a certain season")
    print("4 to show the festivals in which a certain artist performs")
    print("x to exit")

def show_all_festivals(listFestivals):
    for i in listFestivals:
        print(to_str(i))

def show_sorted_festivals_in_season(listFestivals,season):
    if season == "spring":
        months = [3,4,5]
    elif season == "summer":
        months = [6,7,8]
    elif season == "autumn":
        months = [9,10,11]
    elif season == "winter":
        months = [12,1,2]
    listf = []
    for i in listFestivals:
        if get_month(i) in months:
            listf.append(i)
    listsorted = sort_festivals(listf)
    for i in listsorted:
        print(to_str(i))

def show_festival_artist(listFestivals,artist):
    for i in listFestivals:
        for j in get_artists(i):
            if j == artist:
                print(to_str(i))

def start():
    listFestivals = init_festivals()
    while True:
        print(" ")
        print("MENU")
        print_menu()
        print(" ")
        command = input("> ")
        if command == "x":
            return
        elif command == "1":
            show_all_festivals(listFestivals)
        elif command == "2":
            name = input("name = ")
            month = int(input("month = "))
            cost = int(input("ticket cost = "))
            artists = input("artists: ").split(", ")
            try:
                festival = create_festival(name,month,cost,artists)
                add_festival(listFestivals,festival)
            except ValueError as ve:
                print(ve)
        elif command == "3":
            season = input("season = ")
            show_sorted_festivals_in_season(listFestivals,season)
        elif command == "4":
            artist = input("artist = ")
            show_festival_artist(listFestivals,artist)
        else:
            print("Invalid command")

start()