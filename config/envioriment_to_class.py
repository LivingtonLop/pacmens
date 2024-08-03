#imports to class
#Variable Constante
import pygame
import json
import os
#to recurses
from typing import Union
from dotenv import load_dotenv

#CONSTANS
KEY_DOWNS : dict = {pygame.K_DOWN : 90 ,pygame.K_RIGHT : 0,pygame.K_UP : 270,pygame.K_LEFT : 180} 


#COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

#BTNS
BTN_PAUSE_X :int = 600
BTN_PAUSE_y : int= 530

BTN_RETRY_X :int = 700
BTN_RETRY_y : int= 530

COOR_SCORE : tuple = (300,530)