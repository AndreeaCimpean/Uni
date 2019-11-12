def get_name(festival):
    return festival["name"]
def get_month(festival):
    return festival["month"]
def get_ticket_cost(festival):
    return festival["cost"]
def get_artists(festival):
    return festival["artists"]

def create_festival(name,month,cost,artists):
    '''
    Create a festival
    params:
        name - the name of the festival
        month - the month (integer between 1 and 12)
        cost - the ticket cost
        artists - the list of artists which perform
    output:
        the created festival as a dictionary if valid data
        raise an error if invalid data
    '''
    if month < 1 or month > 12:
        raise ValueError("Not a valid month")
    return {"name":name,"month":month,"cost":cost,"artists":artists}

def init_festivals():
    listFestivals = []
    listFestivals.append(create_festival("Untold",7,700,["Martin Garrix","David Guetta","Steve Aoki"]))
    listFestivals.append(create_festival("Tomorrowland",10,800,["David Guetta","Steve Aoki"]))
    listFestivals.append(create_festival("Happiness",10,790,["EDEN","Billie Eilish"]))
    listFestivals.append(create_festival("White",6,500,["Billie Eilish"]))
    listFestivals.append(create_festival("FESTA",5,1200,["BTS"]))
    return listFestivals

def to_str(festival):
    '''
    Return a festival as a string in order to print
    '''
    monthsName = ["0","January","February","March","April","May","June","July","August","September","October","November","December"]
    r = "name: " + get_name(festival) + ", month: " + monthsName[get_month(festival)] + ", ticket cost: " + str(get_ticket_cost(festival)) + ", artists: "
    artists = get_artists(festival)
    r += artists[0]
    for i in range(1,len(artists)):
        r += ", " + artists[i]
    return r

def test_to_str():
    f = create_festival("New",11,100,["Dan","Anna"])
    f2 = create_festival("Yes",12,50,["David"])
    assert to_str(f) == "name: New, month: November, ticket cost: 100, artists: Dan, Anna"
    assert to_str(f2) == "name: Yes, month: December, ticket cost: 50, artists: David"


def test_create_festival():
    f = create_festival("New",11,100,["Dan","Anna"])
    assert get_name(f) == "New" and get_month(f) == 11 and get_ticket_cost(f) == 100 and get_artists(f) == ["Dan","Anna"]
    try:
        f2 = create_festival("Yes",105,50,["David"])
        assert False
    except ValueError:
        assert True

test_create_festival()
test_to_str()