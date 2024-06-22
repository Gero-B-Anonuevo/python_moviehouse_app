import sqlite3

room = [(1, 500), (2, 600), (3, 500), (4, 650)]

database = sqlite3.connect('moviehouse.db')
cursor = database.cursor()

table_creation_room = '''CREATE TABLE IF NOT EXISTS room
        (id INTEGER PRIMARY KEY, cost REAL)
'''

table_creation_movie = '''CREATE TABLE IF NOT EXISTS movie
        (id INTEGER PRIMARY KEY, title VARCHAR, genre VARCHAR, is_deleted BOOLEAN default 0, cost REAL)
'''

database.execute('PRAGMA foreign_keys = ON')
table_creation_room_record = '''CREATE TABLE IF NOT EXISTS room_record
        (id INTEGER PRIMARY KEY, room_id INTEGER, total_cost REAL, is_finished BOOLEAN,
        FOREIGN KEY (room_id) REFERENCES room(id))
'''

table_creation_room_movie_record = '''CREATE TABLE IF NOT EXISTS room_movie_record
        (id INTEGER PRIMARY KEY, movie_id INTEGER, room_record_id INTEGER, 
        FOREIGN KEY (movie_id) REFERENCES movie(id),
        FOREIGN KEY (room_record_id) REFERENCES room_record(id))
'''

database.execute(table_creation_room)
cursor.executemany('''INSERT INTO room (id, cost) VALUES (?, ?)''', room)
database.execute(table_creation_movie)
database.execute(table_creation_room_record)
database.execute(table_creation_room_movie_record)

database.commit()

database.close()

