from domain import *

def find_animal(listAnimals,code):
    '''
    Search if there is an animal with a certain code
    params:
        listAnimals - the list of animals
        code - the code
    output:
        True - there is such an animal
        False - otherwise
    '''
    for i in listAnimals:
        if get_code(i) == code:
            return True
    return False

def add_animal(listAnimals,animal):
    '''
    Add a new animal
    params:
        listAnimals - the list of animals
        animal - the animal
    Add a new animal if valid data(code unique)
    Raise an error otherwise
    '''
    if find_animal(listAnimals,get_code(animal)):
        raise ValueError("Code must be unique")
    listAnimals.append(animal) 

def sort_by_name(listAnimals):
    for i in range(0,len(listAnimals)-1):
        for j in range(i+1,len(listAnimals)):
            if get_name(listAnimals[i]) > get_name(listAnimals[j]):
                aux = listAnimals[i]
                listAnimals[i] = listAnimals[j]
                listAnimals[j] = aux
    return listAnimals

def update_type_for_species(listAnimals,species,atype):
    if len(atype) == 0:
        raise ValueError("Type must not be void")
    for i in listAnimals:
        if get_species(i) == species:
            set_type(i,atype)

def test_find_animal():
    listAnimals = []
    a = create_animal("Z01","Zizi","herbivore","zebra")
    listAnimals.append(a)
    assert find_animal(listAnimals,"Z01")
    assert not find_animal(listAnimals,"A23")

def update_type_for_animal(listAnimals,code,atype):
    '''
    Update the type of a given animal
    params:
        listAnimals - the list of animals
        code - the animal code
        atype - the new type
    Set the type for the animal to a new value
    '''
    for i in listAnimals:
        if get_code(i) == code:
            set_type(i,atype)

def test_add_animal():
    listAnimals = []
    a = create_animal("Z01","Zizi","herbivore","zebra")
    add_animal(listAnimals,a)
    assert listAnimals[0] == a
    try:
        a2 = create_animal("Z01","Sisi","herbivore","zebra")
        add_animal(listAnimals,a2)
        assert False
    except ValueError:
        assert True

def test_update_type_animal():
    listAnimals = []
    a = create_animal("Z01","Zizi","herbivore","zebra")
    listAnimals.append(a)
    update_type_for_animal(listAnimals,"Z01","carnivore")
    assert get_type(listAnimals[0]) == "carnivore"

test_find_animal()
test_add_animal()
test_update_type_animal()