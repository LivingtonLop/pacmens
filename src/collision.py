
class Collision():
    def __init__(self,tile_size:int,form:list) -> None:
        self.tile_size: int = tile_size
        self.form : list = form
        
    def collision(self,rect)->bool:
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
