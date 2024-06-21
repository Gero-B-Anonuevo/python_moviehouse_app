class Movie:
    def __init__(self, id, title, genre, cost):
        self.id = id
        self.title = title
        self.genre = genre
        self.cost = cost

    def __str__(self):
        return f"{self.id} - {self.title}"
    
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_genre(self):
        return self.genre
    
    def get_cost(self):
        return self.cost
    
    def set_id(self, id):
        self.id = id
        return self.id
    
    def set_title(self, title):
        self.title = title
        return self.title
    
    def set_genre(self, genre):
        self.genre = genre
        return self.genre
    
    def set_cost(self, cost):
        self.cost = cost
        return self.cost

class Room:
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost

    def get_id(self):
        return self.id
    
    def get_cost(self):
        return self.cost
    
    def set_id(self, id):
        self.id = id
        return self.id
    
    def set_cost(self, cost):
        self.cost = cost
        return self.cost
#UNSURE ------------------------------------------
class Record:
    def __init__(self, id, room_id, total_cost, movies):
        self.id = id
        self.room_id = room_id
        self.total_cost = total_cost
        self.movies = movies

    def get_id(self):
        return self.id
    
    def get_room_id(self):
        return self.room_id
    
    def get_total_cost(self):
        return self.total_cost
    
    def get_movies(self):
        return self.movies
    
    def set_id(self, id):
        self.id = id
        return self.id
    
    def set_room_id(self, room_id):
        self.room_id = room_id
        return self.room_id
    
    def set_total_cost(self, total_cost):
        self.total_cost = total_cost
        return self.total_cost
    
    def set_movies(self, movies):
        self.movies = movies
        return self.movies


