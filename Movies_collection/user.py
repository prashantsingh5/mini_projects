from movie import Movie

class User:
    def __init__(self,name):
        self.name = name
        self.movies=[]

    def __repr__(self):
        return "<user {}>".format(self.name)
    
    def watched_movies(self):
        movies_watched =list(filter(lambda x: x.watched, self.movies))
        return movies_watched
    
    def add_movie(self,name,genre):
        movies = Movie(name,genre,False)
        self.movies.append(movies)

    def delete_movie(self,name):
        self.movies = list(filter(lambda movie:movie.name != name,self.movies))

    def save_to_file(self):
        with open ("{}.txt".format(self.name),"w") as f:
            f.write("username is {}".format(self.name) + "\n")
            for movies in self.movies:
                f.write('{},{},{}\n'.format(movies.name ,movies.genre, str(movies.watched))) 


    """@classmethod
    def load_from_file(cls,filename):
        with open(filename,'r') as f:
            content=f.readlines()
            username=content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(",")
                movies.append(movie(movie_data[0],movie_data[1],movie_data[2]=='True'))
            users=User(username)
            users.movies = movies
            return users"""
    
    def json(self):
        return {
            'name':self.name,
            'movies':[
                movie.json() for movie in self.movies 
            ]
        }
    
    @classmethod
    def from_json(cls,json_data):
        user=User(json_data['name'])
        movies=[]
        for movie_data in json_data["movies"]:
            movies.append(Movie.from_json(movie_data))
        user.movies=movies
        return user
    
    def set_watched(self,name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True
                