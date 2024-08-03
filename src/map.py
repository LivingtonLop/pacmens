from config.envioriment_to_class import (
                                            pygame,
                                            BLACK,
                                            WHITE,
                                            BLUE
                                        )
from collision import Collision
import random
class Map(Collision):
    
    def __init__(self, level : dict) -> None:

        super().__init__(form=level["map"],tile_size=level["tile_size"])

        self.form : list = level["map"]
        self.tile_size : int = level["tile_size"] 
        self.colors :dict = {
            0 : BLACK,
            1: BLUE
        }
        self.circles, self.apples, self.coins = self.place_items(self.get_open_positions())

    def render(self, surface : pygame)->None:
        for x_index, x in enumerate(self.form):
            for y_index, tile in enumerate(x):
                color = self.colors.get(tile, (0, 0, 0))
                pygame.draw.rect(surface, color, pygame.Rect(y_index * self.tile_size, x_index * self.tile_size, self.tile_size, self.tile_size))


    def place_items(self, open_positions):
        random.shuffle(open_positions)

        apple_count = 0
        coin_count = 0

        circles = []
        apples = []
        coins = []

        for idx, (x, y) in enumerate(open_positions):
            # Store circle positions
            
            # Place apple after every 20 circles
            if idx % 20 == 0 and apple_count < 1:
                
                apples.append((x, y))
                apple_count += 1
            
            # Place coin after every 50 circles
            if idx % 50 == 0 and coin_count < 3:
                if not (x,y) in apples:
                    coins.append((x, y))
                    coin_count += 1

            if not (x,y) in apples and not (x,y) in coins:
                circles.append((x, y))


        return circles, apples, coins
    
    def renderItem(self,surface,apple_image, coin_image):

         # Draw apples
        for (x, y) in self.apples:
            surface.blit(apple_image, (x * self.tile_size, y * self.tile_size))

        # Draw circles
        for (x, y) in self.circles:
            circle_center = (x * self.tile_size + self.tile_size // 2, y * self.tile_size + self.tile_size // 2)
            pygame.draw.circle(surface, (255, 255, 0), circle_center, 5)
        
        # Draw coins
        for (x, y) in self.coins:
            surface.blit(coin_image, (x * self.tile_size, y * self.tile_size))

    