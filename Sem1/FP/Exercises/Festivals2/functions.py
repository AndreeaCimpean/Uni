from domain import *

def find_festival(listFestivals,name):
    '''
    Check if there already exists a festivel with a given name
    params:
        listFestivals - the list of festivals
        name - the given name
    output:
        True - if there exists
        False - otherwise
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
        festival - the given festival
    Add the festival if valid data (name unique)
    Raise an error otherwise
    '''
    if find_festival(listFestivals,get_name(festival)):
        raise ValueError("Festival already exists")
    listFestivals.append(festival)

def sort_festivals(listFestivals):
    for i in range(0,len(listFestivals)-1):
        for j in range(i+1,len(listFestivals)):
            if get_month(listFestivals[i]) > get_month(listFestivals[j]):
                aux = listFestivals[i]
                listFestivals[i] = listFestivals[j]
                listFestivals[j] = aux
            elif get_month(listFestivals[i]) == get_month(listFestivals[j]) and get_name(listFestivals[i]) > get_name(listFestivals[j]):
                aux = listFestivals[i]
                listFestivals[i] = listFestivals[j]
                listFestivals[j] = aux
    return listFestivals

def test_find_festival():
    listFestivals = []
    listFestivals.append(create_festival("New",11,100,["Dan","Anna"]))
    assert find_festival(listFestivals,"New")
    assert not find_festival(listFestivals,"Yes")

def test_add_festival():
    listFestivals = []
    f = create_festival("New",11,100,["Dan","Anna"])
    add_festival(listFestivals,f)
    assert listFestivals[0] == f
    try:
        f2 = create_festival("New",10,300,["David"])
        add_festival(listFestivals,f2)
        assert False
    except ValueError:
        assert True

test_find_festival()
test_add_festival()