from domain import *
from functions import *

def print_menu():
    print("1 add a new festival")
    print("2 show all festivals for a season")
    print("3 show all festivals where an artist will perform")
    print("4 show all festivals")
    print("x to exit")

def show_all_festivals(listFestivals):
    for i in listFestivals:
        print(to_str(i))

def show_all_festivals_season(listFestivals,season):
    if season == "spring":
        months = [3,4,5]
    elif season == "summer":
        months =[6,7,8]
    elif season == "autumn":
        months == [9,10,11]
    elif season == "winter":
        months =[12,1,2]
    
    print(" ")
    listf = []
    for i in listFestivals:
        if get_month(i) in months:
            listf.append(i)
    listsorted = sort_festivals(listf)
    for i in listsorted:
        print(to_str(i))
def show_festival_with_artist(listFestivals,artist):
    print(" ")
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
        #print(listFestivals)
        command = input("> ")
        if command == "x":
            return
        elif command == "1":
            name = input("festival name = ")
            month = int(input("month = "))
            cost = int(input("ticket cost = "))
            artists = input("artists: ").split(",")
            festival = create_festival(name,month,cost,artists)
            try:
                add_festival(listFestivals,festival)
            except ValueError as ve:
                print(ve)
        elif command == "2":
            season = input("season = ")
            show_all_festivals_season(listFestivals,season)
        elif command =="3":
            artist = input("artist = ")
            show_festival_with_artist(listFestivals,artist)
        elif command == "4":
            show_all_festivals(listFestivals)
        else:
            print("Not a valid command")

start()