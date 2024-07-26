import pygame
import math
class Entity:
    def __init__(self, dir_image_sprite : str, pos_x : int ,pos_y : int, scale : tuple = None,dir_image_sprite_2 : str = None) -> None:
        self.img : str = dir_image_sprite #dinamica
        self.img_2 : str = dir_image_sprite_2
        self.x : int= pos_x
        self.y : int= pos_y
        self.scale : tuple = scale
        self.heading : int = 0
        self.animation : bool =  False
        self.target : tuple = None
        self.smarth : int = 5 #max

    def render(self, surface : pygame)-> None:
        img = pygame.image.load(self.img_2 if self.animation else self.img)
        sprite = pygame.transform.scale(img, self.scale)
        tup =(self.x, self.y) 
        if self.heading != 0:
            sprite = pygame.transform.rotate(sprite, self.heading)
            sprite = pygame.transform.flip(sprite,False, True)
            tup = sprite.get_rect(center=(self.x + self.scale[0] // 2, self.y + self.scale[1] // 2)).topleft
        
        surface.blit(sprite,tup)

    def toggle_animation (self)-> None:
        self.animation = not self.animation

    def set_target(self, target_x:int, target_y:int)-> None:
        self.target = (target_x,target_y)

    def follow_target(self)-> None:
        dx = self.target[0] - self.x
        dy = self.target[1] - self.y

        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0:
            dx/=distance
            dy/=distance
            self.x += dx * 3
            self.y += dy * 3


        