class Movie:
    def __init__(self, id, title, genre, cost):
        self.__id = id
        self.title = title
        self.__genre = genre
        self.__cost = cost

    def __str__(self):
        return f"{self.__id} - {self.title}"
    
    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.title
    
    def get_genre(self):
        return self.__genre
    
    def get_cost(self):
        return self.__cost
    
    def set_id(self, id):
        self.__id = id
        return self.__id
    
    def set_title(self, title):
        self.title = title
        return self.title
    
    def set_genre(self, genre):
        self.__genre = genre
        return self.__genre
    
    def set_cost(self, cost):
        self.__cost = cost
        return self.__cost

class Room:
    def __init__(self, id, cost):
        self.__id = id
        self.__cost = cost

    def get_id(self):
        return self.__id
    
    def get_cost(self):
        return self.__cost
    
    def set_id(self, id):
        self.__id = id
        return self.__id
    
    def set_cost(self, cost):
        self.__cost = cost
        return self.__cost

class Record:
    def __init__(self, id, room_id, total_cost, movies: list[Movie], is_finished = True):
        self.__id = id
        self.__room_id = room_id
        self.__total_cost = total_cost
        self.movies = movies
        self.__is_finished = is_finished

    def get_id(self):
        return self.__id
    
    def get_room_id(self):
        return self.__room_id
    
    def get_total_cost(self):
        return self.__total_cost
    
    def get_movies(self):
        return self.movies
    
    def get_is_finished(self):
        return self.__is_finished
    
    def set_id(self, id):
        self.__id = id
        return self.__id
    
    def set_room_id(self, room_id):
        self.__room_id = room_id
        return self.__room_id
    
    def set_total_cost(self, total_cost):
        self.__total_cost = total_cost
        return self.__total_cost
    
    def set_movies(self, movies):
        self.movies = movies
        return self.movies
    
    def set_is_finished(self, is_finished):
        self.__is_finished = is_finished
        return self.__is_finished


