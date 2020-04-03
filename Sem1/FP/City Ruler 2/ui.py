from city import *
from game import *


a = lambda x: [x+1]
b = a(1)
c = lambda x: x + b
d = c([1])
a = 1
b = 3
print (a, b, c(4), d[1])

class UI:
    def __init__(self, g):
        self._game = g

    def start(self):
        print("In year 1, " + str(self._game.get_city()))
        for i in range(2, 6):
            print('\n')
            while True:
                try:
                    buyAcres = int(input("Acres to buy/sell(+/-)-> "))
                    if buyAcres > 0:
                        self._game.buy_acres(buyAcres)
                    elif buyAcres < 0:
                        self._game.sell_acres(buyAcres)
                    break
                except ValueError as ve:
                    print(ve)
            while True:
                try:
                    unitsFeed = int(input("Units to feed the population-> "))
                    self._game.feed_population(unitsFeed)
                    break
                except ValueError as ve:
                    print(ve)
            while True:
                try:
                    plantAcres = int(input("Acres to plant-> "))
                    self._game.plant_acres(plantAcres)
                    break
                except ValueError as ve:
                    print(ve)
            print('\n')

            self._game.update_land_price()
            self._game.update_new_people()
            self._game.harvest()
            self._game.rats_infestation()
            if self._game.is_over() == True:
                print("GAME OVER. Half of your population starved!")
                return
            print("In year " + str(i) + ", " + str(self._game.get_city()))
        if self._game.is_won():
            print("CONGRATS!")
        else:
            print("GAME OVER. You did not do well!")


c = City()
g = Game(c)
ui = UI(g)
ui.start()