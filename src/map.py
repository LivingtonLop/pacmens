from config.envioriment_to_class import (
                                            pygame,
                                            BLACK,
                                            WHITE,
                                            BLUE
                                        )
from collision import Collision
class Map(Collision):
    
    def __init__(self, level : dict) -> None:

        super().__init__(form=level["map"],tile_size=level["tile_size"])

        self.form : list = level["map"]
        self.tile_size : int = level["tile_size"] 
        self.colors :dict = {
            0 : BLACK,
            1: BLUE
        }

    def render(self, surface : pygame)->None:
        for x_index, x in enumerate(self.form):
            for y_index, tile in enumerate(x):
                color = self.colors.get(tile, (0, 0, 0))
                pygame.draw.rect(surface, color, pygame.Rect(y_index * self.tile_size, x_index * self.tile_size, self.tile_size, self.tile_size))
