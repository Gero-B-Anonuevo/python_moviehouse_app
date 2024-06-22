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

    def retrieve_movies(self, genres) -> list [Movie]:
        conn = self.get_connection()
        c = conn.cursor()
        if len(genres) == 0:
            moviesFetched = c.execute("""SELECT 
                                        id, 
                                        title, 
                                        genre, 
                                        cost 
                                    FROM movie
                                    WHERE is_deleted = False
                                    """).fetchall()
        else:
            moviesFetched = c.execute(f"""
                                      SELECT 
                                        id, 
                                        title, 
                                        genre, 
                                        cost 
                                      FROM movie 
                                      WHERE genre in ({",".join("?" * len(genres))}) AND is_deleted = False
                                      """, (genres)
                                      ).fetchall()
        movies = list(map(lambda x: Movie(*x), moviesFetched)) 
        conn.close()
        return movies
    
    def retrieve_rooms(self) -> list[Room]:
        conn = self.get_connection()
        c = conn.cursor()
        rooomsFetched = c.execute('SELECT * FROM room').fetchall() 
        rooms = [Room(*x) for x in rooomsFetched]
        conn.close() 
        return rooms

    def retrieve_record(self, room_id) -> Record:
        conn = self.get_connection()
        c = conn.cursor() # Create a cursor object 
        room_record = c.execute(f"""
                                SELECT * 
                                FROM room_record 
                                WHERE room_id = {room_id} 
                                ORDER BY id DESC 
                                LIMIT 1
                                """).fetchall()
        if len(room_record) == 0:
            return Record(0, room_id, 0, [], True)
        else:
            id, dummy_room_id, total_cost, is_finished = room_record[0] 
            moviesFetched = c.execute(f"""
                                    SELECT 
                                        m.id,
                                        m.title,
                                        m.genre,
                                        m.cost
                                    FROM room_record rr
                                    JOIN room_movie_record rmr
                                        ON rr.id = rmr.room_record_id
                                    JOIN movie m
                                        ON rmr.movie_id = m.id
                                    WHERE rr.is_finished = False AND rr.id = {id}
                      """).fetchall() 
            if len(moviesFetched) == 0: 
                return Record(id, room_id, total_cost, [], True)
            movies = [Movie(*x) for x in moviesFetched]
            return Record(id, room_id, total_cost, movies, is_finished)

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
