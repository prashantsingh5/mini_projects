from user import User
import json
import os

def menu():
    name=input("enter your name")
    filename="{}.txt".format(name)
    if file_exists(filename):
        with open(filename,"r") as f:
            json_data=json.load()
        user=User.from_json(json_data)
    else:
        user=User(name)
    
    user_input=input("enter 'a' to add movie,\n 's' to see the list of movies,\n 'w' to set a movie as watched,\n 'd' to delete, \n'l' to see the list of watched movies,\n 'x' to save, 'q' to quit")
    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("enter the name of movie")
            movie_genre = input("enter the name of genre")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print("name: {} genre: {} watched: {}".format(movie.name,movie.genre,movie.watched))
        elif user_input == 'w':
            movie_name=input("enter the name to set as watched: ")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name=input("enter the movie name to delete: ")
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("name: {} genre: {} watched: {}".format(movie.name,movie.genre,movie.watched))
        elif user_input == 'x':
            with open(filename,'w') as f:
                json.dump(user.json(),f)

        user_input=input("enter 'a' to add movie,\n 's' to see the list of movies,\n 'w' to set a movie as watched,\n 'd' to delete, \n'l' to see the list of watched movies,\n 'x' to save, 'q' to quit")



def file_exists(filename):
    return os.path.isfile(filename)

menu()