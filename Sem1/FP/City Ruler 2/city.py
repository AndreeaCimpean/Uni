class City:
    def __init__(self):
        self.starved = 0
        self.newPeople = 0
        self.population = 100
        self.acres = 1000
        self.harvest = 3
        self.rats = 200
        self.landPrice = 20
        self.grainStocks = 2800
        self.plantedAcres = 0

    @property
    def starved(self):
        return self._starved

    @starved.setter
    def starved(self, value):
        self._starved = value

    @property
    def newPeople(self):
        return self._newPeople

    @newPeople.setter
    def newPeople(self, value):
        self._newPeople = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def acres(self):
        return self._acres

    @acres.setter
    def acres(self, value):
        self._acres = value

    @property
    def harvest(self):
        return self._harvest

    @harvest.setter
    def harvest(self, value):
        self._harvest = value

    @property
    def rats(self):
        return self._rats

    @rats.setter
    def rats(self, value):
        self._rats = value

    @property
    def landPrice(self):
        return self._landPrice

    @landPrice.setter
    def landPrice(self, value):
        self._landPrice = value

    @property
    def grainStocks(self):
        return self._grainStocks

    @grainStocks.setter
    def grainStocks(self, value):
        self._grainStocks = value

    @property
    def plantedAcres(self):
        return self._plantedAcres

    @plantedAcres.setter
    def plantedAcres(self, value):
        self._plantedAcres = value

    def __str__(self):
        s = str(self.starved) + " people starved." + '\n'
        s += str(self.newPeople) + " people came to the city." + '\n'
        s += "City population is " + str(self.population) + '\n'
        s += "City owns " + str(self.acres) + " acres of land." + '\n'
        s += "Harvest was " + str(self.harvest) + " units per acre." + '\n'
        s += "Rats ate " + str(self.rats) + " units." + '\n'
        s += "Land price is " + str(self.landPrice) + " units per acre." + '\n'
        s += '\n' + "Grain stocks are " + str(self.grainStocks) + " units."
        return s