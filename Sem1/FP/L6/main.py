from ui import *
from service import *
from domain import *
import random

movies = []

def generate_movie():
    descriptions = ["Bestseller for 4 weeks","A beautiful story","Think about it"] 
    genres = ["horror","drama","comedy","romance"]
    titles = {"first:":["The","Good"],"second:":["Last","Bad"],"third":["Movie","Chapter"]}

    movieId = 1
    title = "Bla"
    genre = genres[random.randint(0,3)]
    description = "Bla Bla"
    return Movie(movieId,title,description,genre)

def generate_client():
    clientId = random.randint(10000,99999)
    


for i in range(0,11):
    movies.append(generate_movie()) 

s = Service(movies)
print(s.listMovies)
ui = UI(s)
ui.start()
