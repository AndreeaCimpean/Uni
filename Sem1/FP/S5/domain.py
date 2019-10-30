from math import *
# classes
# how do they work in python
# which classes to write and how to turn them into program?
# testing
# validation


'''
Starry night ()
Stars have a location (x,y,z) distance at least 1ly between 2 stars
mass (in solar masses, between [0.1]), apparrent magnitude between [-1,15]
'''

class Location:
    '''
    x,y,z - integers
    '''
    def __init__(self,x,y,z):
        self.X = x
        self.Y = y
        self.Z = z

    # properties without setters are called read-only 
    @property
    def X(self):
        return self._x
    @property
    def Y(self):
        return self._y
    @property               # decorator
    def Z(self):
        return self._z

    @X.setter
    def X(self,value):
        self._x = value

    @Y.setter
    def Y(self,value):
        self._y = value
    
    @Z.setter
    def Z(self,value):
        self._z = value

    def __sub__(self,loc):
        return sqrt((self.X-loc.X)**2+(self.Y-loc.Y)**2+(self.Z-loc.Z)**2)

    def __str__(self):
        return '(' + str(self.X) + ',' + str(self.Y) + ',' + str(self.Z) + ')'

def test_location():
    p = Location(1,2,3) # x,y,z ; function call operator
    assert p.X == 1 and p.Y == 2 and p.Z == 3

    p.X = 10
    assert p.X == 10

    p.Y +=5
    assert p.Y == 7
    assert str(p) == '(10,7,3)'

    '''
    p.get_x()

    # allows me to validate the star's position
    p.set_x() # you run code , so you can validate
    p.set_x(p.get_x() + 50) # ok,but ugly

    # python properties to the resq!
    p.x += 50 # code runs, so you can validate and looks reasonable

    # p._x = 5 no code runs, no validation is possible
    '''

test_location()

class Star:
    '''
    location, mass, magnitude
    '''
    def __init__(self,loc,mass,mag):
        self.Location = loc
        self.Mass = mass
        self.Magnitude = mag

    @property
    def Location(self):
        return self._loc

    @Location.setter
    def Location(self,value):
        self._loc = value

    @property
    def Mass(self):
        return self._mass
    @Mass.setter
    def Mass(self, value):
        if value < 0.1 or value > 50:
            raise ValueError("Mass must be in...")
        self._mass = value
    
    @property
    def Magnitude(self):
        return self._mag
    @Magnitude.setter
    def Magnitude(self,value):
        if value < -1 or value > 15:
            raise ValueError("Mag not in...")
        self._mag = value