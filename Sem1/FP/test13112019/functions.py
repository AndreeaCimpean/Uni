from domain import *

def find_coffee(listCoffee,name):
    for i in listCoffee:
        if get_name(i) == name:
            return True
    return False

def add_coffee(listCoffee,coffee):
    '''
    Add a coffee to the list of coffees
    params:
        listCoffee - the list of cofees
        coffee - the coffe that neds to be added
    Add to listCoffee the new coffee
    '''
    if find_coffee(listCoffee,get_name(coffee)):
        raise ValueError("name must be unique")
    listCoffee.append(coffee)

def sorted(listCoffee):
    for i in range(0,len(listCoffee)-1):
        for j in range(i+1,len(listCoffee)):
            if get_country_of_origin(listCoffee[i]) > get_country_of_origin(listCoffee[j]):
                aux = listCoffee[i]
                listCoffee[i] = listCoffee[j]
                listCoffee[j] = aux
            elif get_country_of_origin(listCoffee[i]) == get_country_of_origin(listCoffee[j]) and get_price(listCoffee[i]) > get_price(listCoffee[j]):
                aux = listCoffee[i]
                listCoffee[i] = listCoffee[j]
                listCoffee[j] = aux
    return listCoffee

def filter_coffees_country_price(listCoffee,country,price):
    listf = []
    for i in listCoffee:
        if get_country_of_origin(i) == country and get_price(i) <= price:
            listf.append(i)
    return listf

def filter_coffees_price(listCoffee,price):
    listf = []
    for i in listCoffee:
        if get_price(i) <= price:
            listf.append(i)
    return listf

def filter_coffees_country(listCoffee,country):
    listf = []
    for i in listCoffee:
        if get_country_of_origin(i) == country:
            listf.append(i)
    return listf

def delete_coffees_country(listCoffee,country):
    copyList = listCoffee.copy()
    listCoffee.clear()
    for i in copyList:
        if get_country_of_origin(i) != country:
            listCoffee.append(i)

def test_add_coffee():
    listCoffee = []
    c = create_coffee("Caffe miel","France",5.5)
    add_coffee(listCoffee,c)
    assert listCoffee[0] == c
    c2 = create_coffee("Caffe","France",5.5)
    add_coffee(listCoffee,c2)
    assert listCoffee[1] == c2

test_add_coffee()