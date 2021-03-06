import os
import json
from random import choice, randint
from datetime import datetime

import model
import crud
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())


movies_in_db = []
for movie in movie_data:

    db_movie = crud.create_movie(movie['title'], movie['overview'], movie['release_date'], movie['poster_path'])
    
    movies_in_db.append(db_movie)

for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)
    
    for n in range(10):
        rand_movie = choice(movies_in_db)
        score = randint(1, 5)

        rating = crud.create_rating(score, user, rand_movie)