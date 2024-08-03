import tkinter as tk
from tkinter import messagebox

from config.envioriment_to_class import BLACK,COOR_SCORE, pygame
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
    
    def show_score(self, screen:pygame, score : int):
        font = pygame.font.SysFont('Arial',24)
        text = font.render(f"Puntuacion: {score}", True, (BLACK))
        screen.blit(text, COOR_SCORE)
