import sqlite3
from classes import Record, Room, Movie

class MovieHouseDatabaseManager:
    def __init__(self, database_file:str):
        self.database_file = database_file

    def get_connection(self):
        return sqlite3.connect(self.database_file)

    def register_movie(self, title, genre, cost) -> bool:
        try:
            db_conn = self.get_connection()
            cursor = db_conn.cursor()
            with db_conn:
                movie_insert_query = '''INSERT INTO movie (title, genre, cost) VALUES (?, ?, ?)'''
                movie_insert_tuple = (title, genre, cost)

                cursor.execute(movie_insert_query, movie_insert_tuple)
            return True
        
        except Exception as error:
            db_conn.rollback()
            return False
        finally:
            db_conn.close()

    def remove_movie(self, id):
        db_conn = self.get_connection()
        cursor = db_conn.cursor()
        with db_conn:
            movie_update_query = '''UPDATE movie SET is_deleted = 1 WHERE id=?'''
            movie_update_tuple = (id,)
            cursor.execute(movie_update_query, movie_update_tuple)
        db_conn.close()

    def retrieve_movies(self, genres:list[str] = []) -> list[Movie]:
        db_conn = self.get_connection()
        cursor = db_conn.cursor()
        if genres == []:
            with db_conn:
                movie_retrieve_query = '''SELECT * FROM movie WHERE is_deleted = 0'''
                movie_retrieve_tuple = (genres, )
                cursor.execute(movie_retrieve_query, movie_retrieve_tuple)
                movie_info = cursor.fetchall()
                db_conn.close()
        else:
            with db_conn:
                movie_retrieve_query = '''SELECT * FROM movie WHERE genre=:genre AND is_deleted = 0'''
                movie_retrieve_tuple = {'genre':genres,}
                cursor.execute(movie_retrieve_query, movie_retrieve_tuple)
                movie_info = cursor.fetchall()
                db_conn.close()

        movie_list = [Movie(*movie_data) for movie_data in movie_info]
        return movie_list
    
    def retrieve_rooms(self) -> list[Room]:
        db_conn = self.get_connection()
        cursor = db_conn.cursor()
        with db_conn:
            room_retrieve_query = '''SELECT * FROM room'''
            cursor.execute(room_retrieve_query)
            room_data = cursor.fetchall()
            db_conn.close()
                 
        rooms_list = [Room(*room_data) for room_data in room_data]
        return rooms_list

    def retrieve_record(self, room_id) -> Record:
        db_conn = self.get_connection()
        cursor = db_conn.cursor()
        try:
            with db_conn:
                get_record_query = '''SELECT * FROM room_record WHERE room_id=? AND is_finished = 0 ORDER BY id DESC LIMIT 1'''
                get_record_tuple = (room_id,)
                cursor.execute(get_record_query, get_record_tuple)
                data = cursor.fetchone()
                if data:
                    record_id, room_id, total_cost, is_finished = data
                    get_movie_record_query = '''SELECT movie.id, movie.title, movie.genre, movie.cost 
                    FROM movie 
                    JOIN room_movie_record 
                    ON movie.id = room_movie_record.movie_id 
                    WHERE room_movie_record.room_record_id = ?''' 
                    get_movie_record_tuple = (record_id,)
                    cursor.execute(get_movie_record_query, get_movie_record_tuple)

                    movie_data = cursor.fetchall()
                    db_conn.close()
                    movies = [Movie(*movie_data) for movie_data in movie_data]

                    return Record(record_id, room_id, total_cost, movies)
                else:
                    db_conn.close()
                    return Record(0, room_id, 0, [])
                
        except Exception as error:
            db_conn.close()
            return None

    def check_in(self, room_id, movies) -> bool:
        db_conn = self.get_connection()
        cursor = db_conn.cursor()
        try:
            with db_conn:
                cost_get_query = '''SELECT cost FROM room WHERE id=?'''
                cost_get_tuple = (room_id,)
                cursor.execute(cost_get_query, cost_get_tuple)
                room_cost = cursor.fetchone()[0]

                room_record_create_query = '''INSERT INTO room_record (room_id, total_cost, is_finished) VALUES (?, ?, ?)'''
                room_record_create_tuple = (room_id, sum([movie.cost for movie in movies])+room_cost, 0)
                cursor.execute(room_record_create_query, room_record_create_tuple)

                room_record_id = cursor.lastrowid

                for movie in movies:
                    room_movie_record_create_query = '''INSERT INTO room_movie_record (movie_id, room_record_id) VALUES (?, ?)'''
                    room_movie_record_create_tuple = (movie.id, room_record_id)
                    cursor.execute(room_movie_record_create_query, room_movie_record_create_tuple)
            return True
        except Exception as error:
            db_conn.rollback()
            return False
        finally:
            db_conn.close()

    def check_out(self, id) -> bool:
        db_conn = self.get_connection()
        cursor = db_conn.cursor()
        try:
            with db_conn:
                update_room_record_query = '''UPDATE room_record SET is_finished = 1 WHERE id=?'''
                update_room_record_tuple = (id,)
                cursor.execute(update_room_record_query, update_room_record_tuple)
                return True
        except Exception as error:
            db_conn.rollback()
            return False
        finally:
            db_conn.close()
