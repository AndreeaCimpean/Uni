'''
We want to use feature-driven deveopment
    - we start implementing a feature and make it work
With what do we start?
    - Add a new client, each client is a physical person having a new id, name and age
'''

'''
1. Write a client class in the domain
    - Client has an ID (set in constructor, read only otherwise)
    - Client has a name of len >= 3 and an age >= 18 (properties)
'''


'''
0. Writing domain classes
1. Unit testing the proper way
2. A new layer? Repository

Assignment 1-5
-----------------
    UI  -> Service -> domain
        -> domain
        
    UI
        - user interface for entire program
    Service
        -functions that solve the problems
    Repository
        - manage the list of domain entities
    Domain
        - entities from problem domain
        
    
    UI  -> Service -> Repository -> Domain
                    -> Domain
        -> Domain

'''
from repository import ClientRepository
from services import ClientService
clientRepo = ClientRepository()
clientService = ClientService(clientRepo)

ui = UI(clientService)
ui.start()