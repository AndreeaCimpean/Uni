'''
the functionality
1. Add a new star to the catalogue (generate some stars)
2. Show all stars, sorted by distance from Sun(0,0,0),mass, app. magnitude
3. Which stars are dangerous for Earth (weight>0, appmagn<3)
'''

# where are all the stars

class Service:
    def __init__(self):
        self._stars = []
    def addStar(self, star):
        '''
        Add the new star to the catalogue
        params:
            star-...
        raise ValueError if new star too close existing ones
        '''
        for s in self._stars:
            if s.Location - star.Location < 1:
                raise ValueError("Stars too close!")
        self._stars.append (star)
        
    def sortStars(self,cmp):
        '''
        sort stars by given param
        params:
            cmp - reference to a comparataor function
        return the sorted list of stars
        '''
        pass
    def dangerousStars(self,mass,mag):
        '''
        return list of dangerous stars
        params:
            mass,mag-mass and magnitude
        '''
