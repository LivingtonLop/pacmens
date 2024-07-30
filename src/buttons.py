import pygame

class Button:
    def __init__(self, pos_x : int, pox_y : int, dir_image_button : str, scale : tuple = (50,50)) -> None:
        self.x : int = pos_x
        self.y : int = pox_y
        self.img = pygame.image.load(dir_image_button)
        self.scale : tuple = scale

    def render (self, surface : pygame) -> None:
        self.img = pygame.transform.scale(self.img,self.scale)
        surface.blit(self.img,(self.x, self.y))

    def setImg(self, dir_image_button : str) -> None:
        self.img = pygame.image.load(dir_image_button)
        