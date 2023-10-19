import tkinter as tk44

class Game(tk.Frame):
    def _init_(self):
        tk.Frame._init_(self)
        self.grid()
        self.master.title('2048')