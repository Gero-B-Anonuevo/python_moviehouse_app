from tkinter import *
from database_manager import MovieHouseDatabaseManager
from classes import Record, Room, Movie
from tkinter import messagebox

class RecordWindow(Toplevel):
    def __init__(self, room: Room, db_manager: MovieHouseDatabaseManager, record: Record):
        self.room = room
        self.db_manager = db_manager
        self.record = record

        super().__init__()

        self.title("Room 1")
        self.geometry("550x500")

        self.movies_label = Label(self, text="Movies")
        self.movies_label.place(x=120, y=25)

        self.to_watch_label = Label(self, text="Movies to watch")
        self.to_watch_label.place(x=350, y=25)

        self.movies_list = Listbox(self, selectmode="single", width=43, height=13)
        self.movies_list.place(x=10, y=50)
        self.movies_list.bind("<<ListboxSelect>>", self.update_add_movie_button())

        self.movies_to_view_list = Listbox(self, selectmode="single", width=43, height=13)
        self.movies_to_view_list.place(x=278, y=50)
        self.movies_to_view_list.bind("<<ListboxSelect>>", self.update_remove_movie_button())

        self.add_movie_button = Button(self, text="Add Movie", command= self.add_movies)
        self.add_movie_button.place(x=100, y=270)

        self.remove_movie_button = Button(self, text="Remove Movie", command= self.remove_movie)
        self.remove_movie_button.place(x=357, y=270)

        self.total_cost = StringVar()
        self.total_cost_label = Label(self,text=self.total_cost)
        self.total_cost_label.place(x=230, y=350)

        self.check_in_button = Button(self, text="Check In", command=self.check_in)
        self.check_in_button.place(x=215, y=410)

        self.check_out_button = Button(self, text="Check Out", command=self.check_out)
        self.check_out_button.place(x=278, y=410)

        self.update_listbox()
        self.update_total_cost()
        self.check_button_state()

    def update_listbox(self):
        self.movies_list.delete(0, 'end')
        self.movies_to_view_list.delete(0, 'end')

        new_data = self.db_manager.retrieve_movies()
        movie_title = [movie.get_title() for movie in self.record.get_movies()]
        unchecked_movies = map(str, [movie for movie in new_data if movie.get_title() not in movie_title])
        self.movies_list.insert('end', *unchecked_movies)

        if self.record.__movies:
            self.movies_to_view_list.insert('end', *self.record.get_movies())

    def update_total_cost(self):
        if self.record.get_total_cost():
            self.total_cost.set(f"Total Cost: {sum([movie.get_cost() for movie in self.record.get_movies()]) + self.room.get_cost()}")

    def check_button_state(self):
        if self.record.get_is_finished() and self.movies_to_view_list.size() > 0:
            self.check_out_button.config(state='disabled')
            self.check_in_button.config(state='normal')
        elif self.record.get_is_finished() and self.movies_to_view_list.size() <= 0:
            self.check_out_button.config(state='normal')
            self.check_in_button.config(state='disabled')
        else:
            self.check_out_button.config(state='disabled')
            self.check_in_button.config(state='disabled')

    def add_movies(self):
        line = self.movies_list.curselection()
        if line:
            movie = self.movies_list.get(line)
            self.movies_to_view_list.insert('end', movie)
            self.movies_list.delete(line)
            self.check_button_state()
            self.update_total_cost()
        else:
            messagebox.showerror(title="Error", message="No movie was selected.")

    def remove_movie(self):
        line = self.movies_to_view_list.curselection()

        if line:
            movie = self.movies_to_view_list.get(line)
            self.movies_list.insert('end', movie)
            self.movies_to_view_list.delete(line)
            self.check_button_state()
            self.update_total_cost()
        else:
            messagebox.showerror(title="Error", message="No movie was selected.")

    def update_add_movie_button(self):
        line = self.movies_list.curselection()
        if line and self.check_out_button.cget("state") != 'normal':
            self.add_movie_button.config(state='normal')
        else:
            self.add_movie_button.config(state='disabled')
    
    def update_remove_movie_button(self, event):
        line = self.movies_to_view_list.curselection()
        if line and self.record.get_is_finished():
            self.remove_movie_button.config(state='normal')
        else:
            self.remove_movie_button.config(state='disabled')

    def check_in(self):
        id_of_selected_movie = [movie_id.split("-")[0].strip() for movie_id in self.movies_to_view_list.get(0, 'end')]
        movies = self.db_manager.retrieve_movies(movie_id=id_of_selected_movie)

        if self.db_manager.check_in(self.room.get_id(), movies):
            self.record = self.db_manager.retrieve_record(self.room.get_id())
            messagebox.showinfo("Check in", "Successfully checked in")
        else:
            messagebox.showerror("Error", "An Error has occured")

        self.update_total_cost()
        self.update_listbox()
        self.check_button_state()

    def check_out(self):
        if self.db_manager.check_out(self.record.get_id()):
            self.record = self.db_manager.retrieve_record(self.room.get_id())
            messagebox.showinfo("Success", "Checked out successfully")
        else:
            messagebox.showerror("Error", "An Erro has occured")
        self.update_total_cost()
        self.update_listbox()
        self.check_button_state()

class MovieHouseWindow(Tk):
    def __init__(self, database_filename):
        self._database_manager = MovieHouseDatabaseManager(database_filename)

        super().__init__()

        # main_window
        self.title("Movie House App")
        self.geometry("550x500")

        # main_frame
        self.main_frame = LabelFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        # rooms_frame
        self.right_frame = Frame(self.main_frame)
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.room_label = Label(self.right_frame, text="Rooms")
        self.room_label.pack()

        self.room1_button = Button(self.right_frame, text="Room 1")
        self.room1_button.pack(fill="both", expand=True)

        self.room2_button = Button(self.right_frame, text="Room 2")
        self.room2_button.pack(fill="both", expand=True)

        self.room3_button = Button(self.right_frame, text="Room 3")
        self.room3_button.pack(fill="both", expand=True)

        self.room4_button = Button(self.right_frame, text="Room 4")
        self.room4_button.pack(fill="both", expand=True)

        # left_frame
        self.left_frame = Frame(self.main_frame)
        self.left_frame.pack(side="left", fill="both", expand=True)

        # upper_frame for register
        self.register_frame = LabelFrame(self.left_frame)
        self.register_frame.pack(side="top", fill="both", expand=True)

        self.register_label = Label(self.register_frame, text="Register")
        self.register_label.pack(pady=5)

        self.top_frame_in_register = Frame(self.register_frame)
        self.top_frame_in_register.pack()

        self.title_label = Label(self.top_frame_in_register, text="Title")
        self.title_label.pack(side="left", pady=5)
        self.movie_title_entry = Entry(self.top_frame_in_register)
        self.movie_title_entry.pack(side="left", pady=5, padx=1)

        self.middle_frame_in_register = Frame(self.register_frame)
        self.middle_frame_in_register.pack()

        self.cost_label = Label(self.middle_frame_in_register, text="Cost")
        self.cost_label.pack(side="left", pady=5)
        self.cost_entry = Entry(self.middle_frame_in_register)
        self.cost_entry.pack(side="left", pady=5, padx=1)
       
        self.bottom_frame_in_register = Frame(self.register_frame)
        self.bottom_frame_in_register.pack()

        self.genre_label = Label(self.bottom_frame_in_register, text="Genre")
        self.genre_label.pack(side="left", pady=5)
        self.genre_entry = Entry(self.bottom_frame_in_register)
        self.genre_entry.pack(side="left", pady=5, padx=1)

        self.button_frame_in_register = Frame(self.register_frame)
        self.button_frame_in_register.pack(fill="x")
        self.add_button = Button(self.button_frame_in_register, text="Add Movie", command= self.add_movie, state='disabled')
        self.add_button.pack(side="right")
        
        # lower_frame for movie selection
        self.movies_frame = LabelFrame(self.left_frame)
        self.movies_frame.pack(side="bottom", fill="both", expand=True)

        self.movies_label = Label(self.movies_frame, text="Movies")
        self.movies_label.pack(pady=5)

        self.movies_list = Listbox(self.movies_frame, selectmode="single", width="35", height="20")
        self.movies_list.pack(side="left")
        self.movies_list("<<ListboxSelect>>", self.update_remove_button())

        self.remove_button = Button(self.movies_frame, text="Remove Movie", command=self.remove_movie, state='disabled')
        self.remove_button.pack(side="bottom")

        self.selection_label = Label(self.movies_frame, text="Genre")
        self.selection_label.pack()

        self.selection_right_frame = Frame(self.movies_frame)
        self.selection_right_frame.pack(fill="both", expand=True, side="right")

        self.selection_left_frame = Frame(self.movies_frame)
        self.selection_left_frame.pack(fill="both", expand=True, side="right")

        self.adventure_val = BooleanVar()
        adventure_checkbutton = Checkbutton(self.selection_left_frame, variable=self.adventure_val, command=self.movies_shown)
        adventure_checkbutton.pack()
        adventure_label = Label(self.selection_right_frame, text="Adventure")
        adventure_label.pack(pady= 2)

        self.comedy_val = BooleanVar()
        comedy_checkbutton = Checkbutton(self.selection_left_frame, variable=self.comedy_val, command=self.movies_shown)
        comedy_checkbutton.pack(side="top")
        comedy_label = Label(self.selection_right_frame, text="Comedy")
        comedy_label.pack(pady= 2)

        self.fantasy_val = BooleanVar()
        fantasy_checkbutton = Checkbutton(self.selection_left_frame, variable=self.fantasy_val, command=self.movies_shown)
        fantasy_checkbutton.pack()
        fantasy_label = Label(self.selection_right_frame, text="Fantasy")
        fantasy_label.pack(pady= 2)

        self.romance_val = BooleanVar()
        romance_checkbutton = Checkbutton(self.selection_left_frame, variable=self.romance_val, command=self.movies_shown)
        romance_checkbutton.pack()
        romance_label = Label(self.selection_right_frame, text="Romance")
        romance_label.pack(pady= 2)

        self.tragedy_val = BooleanVar()
        tragedy_checkbutton = Checkbutton(self.selection_left_frame, variable=self.tragedy_val, command=self.movies_shown)
        tragedy_checkbutton.pack()
        tragedy_label = Label(self.selection_right_frame, text="Tragedy")
        tragedy_label.pack(pady= 2)

        self.update_list()

    def update_list(self):
        self.movies_list.delete(0, 'end')
        movies = self._database_manager.retrieve_movies()
        for movie in movies:
            self.movies_list.insert('end', movie)

    def update_remove_button(self):
        line = self.movies_list.curselection()
        if line:
            self.remove_button.config(state='normal')
        else:
            self.remove_button.config(state='disabled')

    def add_movie(self):
        title = self.movie_title_entry.get()
        genre = self.genre_entry.get()
        cost = self.cost_entry.get()

        if not title or not genre or not cost:
            messagebox.showerror("Error", "Please input data into all entry boxes.")
            return

        try:
            cost = float(cost)
        except ValueError:
            messagebox.showerror("Error", "Please input a proper cost. Only numbers may be inserted.")
            return

        if self._database_manager.register_movie(title, genre, cost):
            self.update_list()
            self.movie_title_entry.delete(0, 'end')
            self.genre_entry.delete(0, 'end')
            self.cost_entry.delete(0, 'end')

    def remove_movie(self):
        line = self.movies_list.curselection()

        if line:
            listbox_index = line[0]
            active_movie = self.movies_list.get(listbox_index).split("-")[0].strip()
            self.movies_list.delete(listbox_index)
            self._database_manager.remove_movie(active_movie)
            self.update_list()

    def movies_shown(self):
        genres = []
        if self.adventure_val.get():
            genres.append("Adventure")
        if self.comedy_val.get():
            genres.append("Comedy")
        if self.fantasy_val.get():
            genres.append("Fantasy")
        if self.romance_val.get():
            genres.append("Romance")
        if self.tragedy_val.get():
            genres.append("Tragedy")

        movies = self._database_manager.retrieve_movies(genres=genres)
        self.movies_list.delete(0, 'end')
        for movie in movies:
            self.movies_list('end', movie)

    def open_room(self, room_id: int):
        rooms = self._database_manager.retrieve_rooms()
    
        if room_id < 1 or room_id > len(rooms):
            messagebox.showerror("Error", "Room does not exist.")
            return
    
        room = rooms[room_id - 1]
        record = self._database_manager.retrieve_record(room.get_id())
        record_window = RecordWindow(room, self._database_manager, record)
        record_window.mainloop()


window = MovieHouseWindow("moviehouse.db")
window.mainloop()