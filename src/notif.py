import tkinter as tk

from tkinter import messagebox

class Notif:
    def __init__(self) -> None:
        pass
    # q have of reference, that in False == Pause and True == Game Over
    def render(self,q : bool, title:str, message : str)->bool:
        self.root = tk.Tk()
        self.title : str = title
        self.message : str = message
        self.root.withdraw()
        res = messagebox.askyesno(self.title, self.message) if q else messagebox.showinfo(self.title, self.message)
        self.root.destroy()
        return res