from config.envioriment_to_class import (
                                            pygame,
                                            BLACK,
                                            WHITE,
                                            BLUE
                                        )

class Map():
    
    def __init__(self, level : dict) -> None:
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

        

    def collision(self,rect : pygame)->bool:
        response : bool = False
        # Verificar colisiones en más puntos alrededor del rectángulo
        points = [
            (rect.left, rect.top),     # esquina superior izquierda
            (rect.right, rect.top),    # esquina superior derecha
            (rect.left, rect.bottom),  # esquina inferior izquierda
            (rect.right, rect.bottom), # esquina inferior derecha
            (rect.centerx, rect.top),  # centro superior
            (rect.centerx, rect.bottom), # centro inferior
            (rect.left, rect.centery),   # centro izquierda
            (rect.right, rect.centery)   # centro derecha
        ]
        for point in points:
            grid_x = point[0] // self.tile_size
            grid_y = point[1] // self.tile_size
            if grid_x < 0 or grid_x >= len(self.form[0]) or grid_y < 0 or grid_y >= len(self.form):
                response =  True
            if self.form[grid_y][grid_x] == 1:
                response = True
        return response