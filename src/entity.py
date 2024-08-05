import pygame
import math
import random
from map import Map
class Entity (pygame.sprite.Sprite):
    def __init__(self,list_dir_sprite : list [:str], pos_x, pos_y, scale:tuple, enemies : bool = False) -> None:
        super().__init__() 
        self.images : list [:pygame] = [self.load_image_sprite(filename,scale) for filename in list_dir_sprite] #list
        self.index :int = 0
        self.image : pygame = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(pos_x,pos_y))
        self.speed : int = 5
        self.animation : bool = False
        self.heading : int = 0
        self.enemies :bool= enemies
        

    def move(self, x:int,y:int, map : Map):
        new = self.rect.move(x,y)
        if not map.collision(new):
            self.rect = new
        elif self.enemies:
            new = self.rect.move(y,x)
            if not map.collision(new):
                self.rect = new
            else:
                new = self.rect.move(x,y)
                if not map.collision(new):
                    self.rect = new

        
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

    def set_target(self, target : tuple)-> None:
        self.target = target

    def follow_target(self, map : Map, other_entities :list)-> bool: #collsion
        #target
        tx = self.target[0]//map.tile_size  #target
        ty = self.target[1]//map.tile_size  #target
        #entity
        ex = self.rect.x//map.tile_size #entity
        ey = self.rect.y//map.tile_size #entity
        #Persecucion para ir de punto a a punto b
        if tx == ex and not map.collision(self.rect):
            if ty < ey:
                l = -self.speed
            else:
                l = +self.speed
            self.move(0,l, map)
        
        elif ty == ey and not map.collision(self.rect):

            if tx < ex:
                l = -self.speed
            else:
                l = +self.speed
            self.move(l,0, map)
        
        else:
            if abs(tx - ex) > abs(ty - ey):  # Priorizar movimiento en X
                if tx < ex:
                    l = -self.speed
                else:
                    l = self.speed
                self.move(l, 0, map)
            else:  # Priorizar movimiento en Y
                if ty < ey:
                    l = -self.speed
                else:
                    l = self.speed
                self.move(0, l, map)

    # Evitar solapamiento con otros fantasmas
        for entity in other_entities:
            if entity != self and self.rect.colliderect(entity.rect):
                if self.rect.x < entity.rect.x:
                    self.rect.x -= self.speed
                else:
                    self.rect.x += self.speed
                if self.rect.y < entity.rect.y:
                    self.rect.y -= self.speed
                else:
                    self.rect.y += self.speed

        return (tx,ty) == (ex,ey)
    
    def render(self, surface : pygame):
        surface.blit(self.image, self.rect)
