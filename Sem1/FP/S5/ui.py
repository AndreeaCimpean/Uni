from service import Service
class UI:
    # Can the UI do its job without Service? 
    # no, it does not make sense to create a UI without having a Service
     
    def __init__(self,service):
        self._service = service

    def addStar(self):
        # read star location, mass, magnitude
        # check if valid star
        # call service addStar(newStar)

        newStar = None
        self._service.addStar(newStar)
        pass
    def sortStar(self):
        pass
    def start(self):
        # print menu, read user choice, bla, bla ,bla
        # call addStar and sortStars methods
        print('Welcome to star catalogue')

s = Service()
ui = UI(s)
ui.start()