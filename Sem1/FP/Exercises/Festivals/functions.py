from domain import *

def find_festival(listFestivals,name):
    '''
    Find if a name of a festival exists in the list of festivals
    params:
        listFestivals - the list of festivals
        name - the name to search
    output:
        true - found
        false - otherwise
    '''
    for i in listFestivals:
        if get_name(i) == name:
            return True
    return False

def add_festival(listFestivals,festival):
    '''
    Add a new festival to the list of festivals
    params:
        listFestivals - the list of festivals
        name - the name of the festival to add
        month - the month
        cost - the ticket cost
        artists - the list of artists
    Add the festival if the festival does not already exist(name is not unique)
    Raise an error otherwise
    '''
    if find_festival(listFestivals,get_name(festival)):
        raise ValueError("Festival already exists")
    listFestivals.append(festival)

def sort_festivals(listf):
    for i in range (0,len(listf)-1):
        for j in range (i+1,len(listf)):
            if get_month(listf[i]) > get_month(listf[j]):
                aux = listf[i]
                listf[i] = listf[j]
                listf[j] = aux
            elif get_month(listf[i]) == get_month(listf[j]) and get_name(listf[i]) > get_name(listf[j]):
                aux = listf[i]
                listf[i] = listf[j]
                listf[j] = aux
    return listf
    
def test_find_festival():
    listFestivals = []
    listFestivals.append(create_festival("New",12,100,["Anna"]))
    assert find_festival(listFestivals,"New")
    assert not find_festival(listFestivals,"Vara")

def test_add_festival():
    listFestivals = []
    f = create_festival("New",12,100,["Anna"])
    add_festival(listFestivals,f)
    assert listFestivals[0] == f
    try:
        f2 = create_festival("New",11,200,["Mara"])
        add_festival(listFestivals,f2)
        False
    except ValueError:
        True
    

test_find_festival()
test_add_festival()