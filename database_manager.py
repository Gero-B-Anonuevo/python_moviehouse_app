import sqlite3

db_conn = ""

class MovieHouseDatabaseManager:
    def __init__(self, database_file:str):
        self.database_file = database_file

    def get_connection():
        global db_conn
        db_conn = sqlite3.connect('moviehouse.db')
#UNSURE ---------------------------------------------------
    def register_movie(self, title, genre, cost) -> bool:
        self.get_connection()
        movie_insert_query = '''INSERT INTO movie (title, genre, cost) VALUES (?, ?, ?)'''
        movie_insert_tuple = (title, genre, cost)

        cursor = db_conn.cursor()
        cursor.execute(movie_insert_query, movie_insert_tuple)
        db_conn.commit()
        db_conn.close()

    def remove_movie(id):
        pass
        #hahanapin niya yung row na equal yung id na var sa id na column. tas gawing true si is_deleted

    def retrieve_movies(genres):
        pass
        #i re read ule yung db, hanapin yung row na equal is genres var at column an genres.
        #kunin lahat ng movies. kapag walang output lahat ng movie ibigay