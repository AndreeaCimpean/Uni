import random

class Game:
    def __init__(self, city):
        self._city = city

    def get_city(self):
        return self._city

    def buy_acres(self, acres):
        if self._city.landPrice * acres > self._city.grainStocks:
            raise ValueError("You cannot buy more land than you have grain for!")
        self._city.grainStocks -= self._city.landPrice * acres
        self._city.acres += acres

    def sell_acres(self, acres):
        if self._city.acres < acres:
            raise ValueError("You cannot sell more land than you have!")
        self._city.grainStocks += self._city.landPrice * acres
        self._city.acres -= acres

    def feed_population(self, grains):
        if grains > self._city.grainStocks:
            raise ValueError("You cannot feed people with grain you do not have!")
        self._city.grainStocks -= grains
        feeded = grains//20
        self._city.starved = self._city.population - feeded
        self._city.population -= self._city.starved

    def plant_acres(self, acres):
        if self._city.acres < acres:
            raise ValueError("You cannot plant more acres than you have!")
        if self._city.grainStocks < acres:
            raise ValueError("You cannot plant grain that you do not have!")
        self._city.grainStocks -= acres
        self._city.plantedAcres = acres

    def update_land_price(self):
        self._city.landPrice = random.randint(15, 25)

    def update_new_people(self):
        if self._city.starved == 0:
            self._city.newPeople = random.randint(0, 10)
        self._city.population += self._city.newPeople

    def harvest(self):
        self._city.harvest = random.randint(1, 6)
        if self._city.population * 10 > self._city.plantedAcres:
            self._city.grainStocks += self._city.plantedAcres * self._city.harvest
        else:
            self._city.grainStocks += self._city.population * 10 * self._city.harvest

    def rats_infestation(self):
        chance = random.randint(1, 10)
        if chance == 1 or chance == 2:
            rate = random.randint(1, 10)
            self._city.rats = rate//100 * self._city.grainStocks
            self._city.grainStocks -= self._city.rats
        else:
            self._city.rats = 0

    def is_over(self):
        return (self._city.population + self._city.starved)//2 <= self._city.starved

    def is_won(self):
        return self._city.population > 100 and self._city.acres > 1000
