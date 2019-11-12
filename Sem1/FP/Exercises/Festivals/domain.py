def get_name(festival):
    return festival["name"]
def get_month(festival):
    return festival["month"]
def get_cost(festival):
    return festival["cost"]
def get_artists(festival):
    return festival["artists"]

def create_festival(name,month,cost,artists):
    '''
    Create a new festival
    params:
        name - the name of the festival
        month - the month (integer between 1 and 12)
        cost - the ticket cost (integer)
        artists - a list of artists that perform
    Create the festival if valid data
    Raise an error otherwise
    '''
    if month < 1 or month > 12:
        raise ValueError("Not a valid month")
    return {"name":name,"month":month,"cost":cost,"artists":artists}

def init_festivals():
    listFestivals = []
    listFestivals.append(create_festival("YAY",7,300,["Bruno Mars"]))
    listFestivals.append(create_festival("Untold",7,700,["Martin Garrix","Steve Aoki"]))
    listFestivals.append(create_festival("Tomorrowland",10,500,["Martin Garrix","Avicii"]))
    listFestivals.append(create_festival("FESTA",6,400,["EDEN"]))
    listFestivals.append(create_festival("Happiness",3,760,["Billie Eilish","EDEN"]))
    return listFestivals

def to_str(festival):
    '''
    Return the festival as a string in order to print it
    '''
    monthsName = ["0","January","February","March","April","May","June","July","August","September","October","November","December"]
    r = festival["name"] + ", month: " + monthsName[festival["month"]] + ", ticket costs: " + str(festival["cost"]) + ", artists: "
    for i in range (0,len(festival["artists"])-1):
        r+= festival["artists"][i] + ", "
    r+= festival["artists"][len(festival["artists"])-1]
    return r

def test_create_festival():
    f = create_festival("Vara",11,100,["Inna"])
    assert get_name(f) == "Vara" or get_month(f) == 11 or get_cost(f) == 100 or get_artists(f) == ["Inna"]
    try:
        f2 = create_festival("Iarna",21,90,["Stefan Hrusca"])
        False
    except ValueError:
        assert True

def test_to_str():
    f = create_festival("Vara",11,100,["INNA","Stefan Hrusca"])
    festival = to_str(f)
    assert festival == "Vara, month: November, ticket costs: 100, artists: INNA, Stefan Hrusca"

test_create_festival()
test_to_str()    