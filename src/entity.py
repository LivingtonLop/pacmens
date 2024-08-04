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
        self.moving_down = True
        self.moving_right = True

    def move(self, x:int,y:int, map : Map):
        new = self.rect.move(x,y)
        if not map.collision(new):
            self.rect = new
        # else:
        #     if self.enemies:
        #         new = self.rect.move(x-random.randint(1,20),y)
        #         if not map.collision(new):
        #             self.rect = new
        #         new = self.rect.move(x+random.randint(1,20),y)
        #         if not map.collision(new):
        #             self.rect = new
        #         new = self.rect.move(x,y-random.randint(1,20))
        #         if not map.collision(new):
        #             self.rect = new
        #         new = self.rect.move(x,y+random.randint(1,20))
        #         if not map.collision(new):
        #             self.rect = new
                

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
        tx = self.target[0]//map.tile_size  #target
        ex = self.rect.x//map.tile_size #entity
        ty = self.target[1]//map.tile_size  #target
        ey = self.rect.y//map.tile_size #entity
        open_pos = map.get_open_positions()
        min_x = min(open_pos,key=lambda tupla : tupla[0])[0]
        max_x = max(open_pos,key=lambda tupla : tupla[0])[0]

        min_y = min(open_pos,key=lambda tupla : tupla[1])[1]
        max_y = max(open_pos,key=lambda tupla : tupla[1])[1]

        l = 0
        #logica para ir de punto a a punto b
        if tx == ex:
            if ty < ey:
                l = -3
            else:
                l = +3
            self.move(0,l, map)
        if ty == ey:

            if tx < ex:
                l = -3
            else:
                l = +3
            self.move(l,0, map)

        else:
            # Almacenar la posición anterior
            previous_pos = self.rect
            # Determinar rango de movimiento
            x_range = abs(max_x - min_x)
            y_range = abs(max_y - min_y)
        # Verificar si se puede mover en x o en y
            if map.can_move_in_x(self.rect, x_range):
                # Movimiento horizontal
                if self.moving_right:
                    self.rect[0] += self.speed
                    if self.rect[0] >= max_x*map.tile_size or map.collision(self.rect):
                        self.rect = previous_pos  # Restaurar posición anterior en caso de colisión
                        self.moving_right = False
                else:
                    self.rect[0] -= self.speed
                    if self.rect[0] <= min_x*map.tile_size or map.collision(self.rect):
                        self.rect = previous_pos  # Restaurar posición anterior en caso de colisión
                        self.moving_right = True
            elif map.can_move_in_y(self.rect, y_range):
                # Movimiento vertical
                if self.moving_down:
                    self.rect[1] += self.speed
                    if self.rect[1] >= max_y*map.tile_size or map.collision(self.rect):
                        self.rect = previous_pos  # Restaurar posición anterior en caso de colisión
                        self.moving_down = False
                else:
                    self.rect[1] -= self.speed
                    if self.rect[1] <= min_y*map.tile_size or map.collision(self.rect):
                        self.rect = previous_pos  # Restaurar posición anterior en caso de colisión
                        self.moving_down = True
            
            

    def render(self, surface : pygame):
        surface.blit(self.image, self.rect)
