def get_code(animal):
    return animal["code"]
def get_name(animal):
    return animal["name"]
def get_type(animal):
    return animal["type"]
def get_species(animal):
    return animal["species"]

def set_type(animal,atype):
    animal["type"] = atype

def create_animal(code,name,atype,species):
    '''
    Create a new animal
    params:
        code - the code of the animal
        name - the name of the animal
        type - the type
        species - the species
    Return the new animal as a dictionary if valid data(all properties not void)
    Raise an error otherwise
    '''
    if len(code) == 0:
        raise ValueError("Code must not be void")
    if len(name) == 0:
        raise ValueError("Name must not be void")
    if len(atype) == 0:
        raise ValueError("Type must not be void")
    if len(species) == 0:
        raise ValueError("Species must not be void")
    return {"code":code,"name":name,"type":atype,"species":species}

def to_str(animal):
    '''
    Return the animal as a string in order to print
    '''
    return "code: " + get_code(animal) + ", name: " + get_name(animal) + ", type: " + get_type(animal) + ", species: " + get_species(animal)

def init_animals():
    listAnimals = []
    listAnimals.append(create_animal("Z01","Zizi","herbivore","zebra"))
    listAnimals.append(create_animal("B01","Martin","herbivore","bear"))
    listAnimals.append(create_animal("M01","Momo","herbivore","monkey"))
    listAnimals.append(create_animal("T05","Tiki","carnivore","tiger"))
    listAnimals.append(create_animal("Z24","Zizi","herbivore","zebra"))
    return listAnimals

def test_create_animal():
    a = create_animal("Z01","Zizi","herbivore","zebra")
    assert get_code(a) == "Z01" and get_name(a) == "Zizi" and get_type(a) == "herbivore" and get_species(a) == "zebra"
    try:
        create_animal("","Zizi","hebivore","zebra")
        assert False
    except ValueError:
        assert True
    try:
        create_animal("Z02","","hebivore","zebra")
        assert False
    except ValueError:
        assert True

def test_to_str():
    a = create_animal("Z01","Zizi","herbivore","zebra")
    assert to_str(a) == "code: Z01, name: Zizi, type: herbivore, species: zebra"
    b = create_animal("B01","Martin","herbivore","bear")
    assert to_str(b) == "code: B01, name: Martin, type: herbivore, species: bear"    


test_to_str()
test_create_animal()