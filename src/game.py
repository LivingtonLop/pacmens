from config.envioriment_to_class import pygame, WHITE
from events import Events
class Game(Events):
    
    def __init__(self) -> None:
        super().__init__()
        size : tuple = (self.surface_width,self.surface_height)
        pygame.font.init() 
        self.surface = pygame.display.set_mode(size=size) #SURFACE_WIGTH TUPLE WITH SURFACE_HEIGH px
        pygame.display.set_caption(self.surface_name)
        
        self.clock = pygame.time.Clock()
        
        self.score : int = 0

    def run(self):

        while self.to_execute:
            self.event()
            self.update()
            self.render()
            self.clock.tick(15)

        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.to_execute = False
            self.mouse(event=event)
            if not self.to_pause:
                self.keyboard(event=event)
        if not self.to_pause:
            self.pressed() #tiene que siempre usar el get_pressed()

    def update(self):
        pos_pacman = (self.pacman.rect.x//self.map.tile_size,self.pacman.rect.y//self.map.tile_size)

        if not self.to_pause:
            self.all_sprite_pacman.update()

            # #enemigies
            self.enemies_blue.set_target((self.pacman.rect.x,self.pacman.rect.y))
            self.kill_player = self.enemies_blue.follow_target(self.map,self.other_entities)

            self.enemies_pink.set_target((self.pacman.rect.x,self.pacman.rect.y))
            self.kill_player = self.enemies_pink.follow_target(self.map,self.other_entities)
            
            self.enemies_red.set_target((self.pacman.rect.x,self.pacman.rect.y))
            self.kill_player = self.enemies_red.follow_target(self.map,self.other_entities)
            
            self.enemies_yellow.set_target((self.pacman.rect.x,self.pacman.rect.y))
            self.kill_player = self.enemies_yellow.follow_target(self.map,self.other_entities)
        
            if pos_pacman in self.map.circles :
                self.map.circles.remove(pos_pacman)
                self.score+=1

            if pos_pacman in self.map.apples :
                self.map.apples.remove(pos_pacman)
                self.score+=10 #more points

            if pos_pacman in self.map.coins :
                self.map.coins.remove(pos_pacman)
                self.score+=5 #more point

            if self.kill_player:
                if self.notif.render(True,"Game Over","You Loser, press yes to replay or no to close game"):
                    self.to_execute = False
                else:
                    self.resetExcute()

    def render(self):
        self.surface.fill((WHITE))
        #map
        self.map.render(surface=self.surface)

        #items
        self.map.renderItem(self.surface,self.image_apple, self.image_coin)

        #entitys
        self.all_sprite_pacman.draw(self.surface)
        
        self.enemies_blue.render(surface=self.surface)
        self.enemies_red.render(surface=self.surface)
        self.enemies_pink.render(surface=self.surface)
        self.enemies_yellow.render(surface=self.surface)

        #buttons
        self.button_retry.render(surface=self.surface)
        self.button_pause.render(surface=self.surface)
        self.notif.show_score(screen=self.surface,score=self.score)

        pygame.display.update()

    
