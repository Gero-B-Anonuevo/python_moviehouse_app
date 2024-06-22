import tkinter as tk
from database_manager import MovieHouseDatabaseManager
from classes import Record, Room, Movie

main_window = tk.Tk()
main_window.title("Movie House App")
main_window.geometry("550x500")

main_frame = tk.LabelFrame(main_window)
main_frame.pack(fill="both", expand=True)

right_frame = tk.Frame(main_frame)
right_frame.pack(side="right", fill="both", expand=True)

room_label = tk.Label(right_frame, text="Rooms")
room_label.pack()

room1_button = tk.Button(right_frame, text="Button 1")
room1_button.pack(fill="both", expand=True)

room2_button = tk.Button(right_frame, text="Button 2")
room2_button.pack(fill="both", expand=True)

room3_button = tk.Button(right_frame, text="Button 3")
room3_button.pack(fill="both", expand=True)

room4_button = tk.Button(right_frame, text="Button 4")
room4_button.pack(fill="both", expand=True)

left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", fill="both", expand=True)

register_frame = tk.LabelFrame(left_frame)
register_frame.pack(side="top", fill="both", expand=True)

register_label = tk.Label(register_frame, text="Register")
register_label.pack(pady=5)

top_frame_in_register = tk.Frame(register_frame)
top_frame_in_register.pack()

title_label = tk.Label(top_frame_in_register, text="Title")
title_label.pack(side="left", pady=5)
movie_title_entry = tk.Entry(top_frame_in_register)
movie_title_entry.pack(side="left", pady=5, padx=1)

middle_frame_in_register = tk.Frame(register_frame)
middle_frame_in_register.pack()

cost_label = tk.Label(middle_frame_in_register, text="Cost")
cost_label.pack(side="left", pady=5)
cost_entry = tk.Entry(middle_frame_in_register)
cost_entry.pack(side="left", pady=5, padx=1)

bottom_frame_in_register = tk.Frame(register_frame)
bottom_frame_in_register.pack()

genre_label = tk.Label(bottom_frame_in_register, text="Genre")
genre_label.pack(side="left", pady=5)
genre_entry = tk.Entry(bottom_frame_in_register)
genre_entry.pack(side="left", pady=5, padx=1)

button_frame_in_register = tk.Frame(register_frame)
button_frame_in_register.pack(fill="x")
add_button = tk.Button(button_frame_in_register, text="Add Movie")
add_button.pack(side="right")

movies_frame = tk.LabelFrame(left_frame)
movies_frame.pack(side="bottom", fill="both", expand=True)

movies_label = tk.Label(movies_frame, text="Movies")
movies_label.pack(pady=5)

movies_list = tk.Listbox(movies_frame, selectmode="single", width="35", height="20")
movies_list.pack(side="left")

remove_button = tk.Button(movies_frame, text="Remove Movie")
remove_button.pack(side="bottom")

selection_label = tk.Label(movies_frame, text="Genre")
selection_label.pack()

selection_right_frame = tk.Frame(movies_frame)
selection_right_frame.pack(fill="both", expand=True, side="right")

selection_left_frame = tk.Frame(movies_frame)
selection_left_frame.pack(fill="both", expand=True, side="right")

adventure_checkbutton = tk.Checkbutton(selection_left_frame)
adventure_checkbutton.pack()
adventure_label = tk.Label(selection_right_frame, text="Adventure")
adventure_label.pack(pady= 2)

comedy_checkbutton = tk.Checkbutton(selection_left_frame)
comedy_checkbutton.pack(side="top")
comedy_label = tk.Label(selection_right_frame, text="Comedy")
comedy_label.pack(pady= 2)

fantasy_checkbutton = tk.Checkbutton(selection_left_frame)
fantasy_checkbutton.pack()
fantasy_label = tk.Label(selection_right_frame, text="Fantasy")
fantasy_label.pack(pady= 2)

romance_checkbutton = tk.Checkbutton(selection_left_frame)
romance_checkbutton.pack()
romance_label = tk.Label(selection_right_frame, text="Romance")
romance_label.pack(pady= 2)

tragedy_checkbutton = tk.Checkbutton(selection_left_frame)
tragedy_checkbutton.pack()
tragedy_label = tk.Label(selection_right_frame, text="Tragedy")
tragedy_label.pack(pady= 2)

main_window.mainloop()

# room1_record_window = tk.Tk()
# room1_record_window.title("Room 1")
# room1_record_window.geometry("550x500")

# r1_movies_label = tk.Label(room1_record_window, text="Movies")
# r1_movies_label.place(x=120, y=25)

# r1_to_watch_label = tk.Label(room1_record_window, text="Movies to watch")
# r1_to_watch_label.place(x=350, y=25)

# r1_movies_list = tk.Listbox(room1_record_window, selectmode="single", width=43, height=13)
# r1_movies_list.place(x=10, y=50)

# r1_movies_to_view_list = tk.Listbox(room1_record_window, selectmode="single", width=43, height=13)
# r1_movies_to_view_list.place(x=278, y=50)

# add_movie_button = tk.Button(room1_record_window, text="Add Movie")
# add_movie_button.place(x=100, y=270)

# remove_movie_button = tk.Button(room1_record_window, text="Remove Movie")
# remove_movie_button.place(x=357, y=270)

# total_cost_label = tk.Label(room1_record_window,text="Total Cost: ?????")
# total_cost_label.place(x=230, y=350)

# check_in_button = tk.Button(room1_record_window, text="Check In")
# check_in_button.place(x=215, y=410)

# check_out_button = tk.Button(room1_record_window, text="Check Out")
# check_out_button.place(x=278, y=410)

# room1_record_window.mainloop()

# class RecordWindow(tk.Toplevel):
#     def __init__(self, room: Room, db_manager: MovieHouseDatabaseManager, record: Record):
#         self.room = room
#         self.db_manager = db_manager
#         self.record = record

