import pygame
class Entity:
    def __init__(self, dir_image_sprite : str,pos_x : int ,pos_y : int, scale : tuple = (30,30)) -> None:
        self.img : str = dir_image_sprite #dinamica
        self.x : int= pos_x
        self.y : int= pos_y
        self.scale : tuple = scale

    def render(self, surface : pygame):
        img = pygame.image.load(self.img)
        sprite = pygame.transform.scale(img, self.scale)
        surface.blit(sprite,(self.x,self.y))

