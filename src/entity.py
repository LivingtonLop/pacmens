import pygame
import math
from map import Map
class Entity (pygame.sprite.Sprite):
    def __init__(self,list_dir_sprite : list [:str], pos_x, pos_y, scale:tuple) -> None:
        super().__init__() 
        self.images : list [:pygame] = [self.load_image_sprite(filename,scale) for filename in list_dir_sprite] #list
        self.index :int = 0
        self.image : pygame = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(pos_x,pos_y))
        self.speed : int = 5
        self.animation : bool = False
        self.heading : int = 0

    def move(self, x:int,y:int, map : Map):
        new = self.rect.move(x,y)
        if not map.collision(new):
            self.rect = new
        else:
            pass #add logic para evitar atasco
        self.transform()    

    def update(self):
        if self.animation:
            n = len(self.images)
            self.index = (self.index + 1) % n #residuio de index con n (index == 1 + 1)=> 2%2 => 0 else index = 0 1%2 => 1
            self.image = self.images[self.index]
    
        self.transform()    

    @staticmethod
    def load_image_sprite(filename:str, scale:tuple)->pygame:
        return pygame.transform.scale(pygame.image.load(filename),scale)

    def set_animation(self):
        self.animation = not self.animation

    def transform (self):
        if self.heading != 0:
            self.image = pygame.transform.rotate(self.image, self.heading)
            self.image = pygame.transform.flip(self.image,False, True)

    #ai
    def set_target(self, target : tuple)-> None:
        self.target = target

    def follow_target(self, map : Map)-> None:
        dx = self.target[0] - self.rect.x
        dy = self.target[1] - self.rect.y

        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            dx/=distance
            dy/=distance
            self.move(dx * 3,dy * 3, map)

    def render(self, surface : pygame):
        surface.blit(self.image, self.rect)