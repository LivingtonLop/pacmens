from config.envioriment_to_class import pygame, WHITE
from events import Events
class Game(Events):
    
    def __init__(self) -> None:
        super().__init__()
        size : tuple = (self.surface_width,self.surface_height)

        self.surface = pygame.display.set_mode(size=size) #SURFACE_WIGTH TUPLE WITH SURFACE_HEIGH px
        pygame.display.set_caption(self.surface_name)
        
        self.clock = pygame.time.Clock()


    def run(self):
        while self.to_execute:
            self.event()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.to_execute = False

    def update(self):
        if not self.to_pause:
            pass

    def render(self):
        self.surface.fill((WHITE))
        pygame.display.update()