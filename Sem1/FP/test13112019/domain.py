def get_name(coffee):
    return coffee["name"]
def get_country_of_origin(coffee):
    return coffee["country"]
def get_price(coffee):
    return coffee["price"]

def set_name(coffee,name):
    coffee["name"] = name
def set_country_of_origin(coffee,country):
    coffee["country"] = country
def set_price(coffee,price):
    coffee["price"] = price


def create_coffee(name,country,price):
    '''
    Create a new coffee
    params:
        name - cofee name
        country - the country of origin
        price - the price
    Return the cofee as a dictionary if valid data (price - float > 0)
    Raise an error otherwise 
    '''
    if price <= 0 :
        raise ValueError("Not a valid price")
    return {"name":name,"country":country,"price":price}

def init_list():
    '''
    Initial list of coffees
    '''
    listCoffee = []
    listCoffee.append(create_coffee("Caffe miel","France",5.5))
    listCoffee.append(create_coffee("Caffe Machiatto","Italy",6.5))
    listCoffee.append(create_coffee("Latte","Italy",5.5))
    listCoffee.append(create_coffee("Espresso","Germany",2.5))
    listCoffee.append(create_coffee("Caffe Z","France",7.5))
    return listCoffee

def to_str(coffee):
    return "name: " + get_name(coffee) + ", country of origin: " + get_country_of_origin(coffee) + ", price:" + str(get_price(coffee))


def test_create_coffee():
    c = create_coffee("Caffe miel","France",5.5)
    assert get_name(c) == "Caffe miel" and get_country_of_origin(c) == "France" and get_price(c) == 5.5
    try:
        c2 = create_coffee("Caffe 1","Italy",-1.7)
        assert False
    except ValueError:
        assert True

test_create_coffee()