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

            self.keyboard(event=event)
            self.mouse(event=event)


    def update(self):
        if not self.to_pause:
            pass

    def render(self):
        self.surface.fill((WHITE))
        #map
        self.map.render(surface=self.surface)
        #entitys
        self.pacman.render(surface=self.surface)

        self.enemies_blue.render(surface=self.surface)
        self.enemies_pink.render(surface=self.surface)
        self.enemies_red.render(surface=self.surface)
        self.enemies_yellow.render(surface=self.surface)

        #buttons
        self.button_retry.render(surface=self.surface)
        self.button_pause.render(surface=self.surface)

        pygame.display.update()