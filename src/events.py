from config.envioriment_to_class import (
                                            pygame,
                                            KEY_DOWNS
                                        )

from recurses_to_class import ResourcesToClass

class Events(ResourcesToClass):
    
    def __init__(self, ) -> None:
        super().__init__()
        self.tuple_keyboard : tuple = KEY_DOWNS
        
    def keyboard (self,event : pygame) -> None:
        if event.type == pygame.KEYDOWN:
            pass

    def mouse (self,event : pygame) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if self.button_retry.x <= mouse_x <= self.button_retry.x + self.button_retry.img.get_width() and self.button_retry.y <= mouse_y <= self.button_retry.y + self.button_retry.img.get_height():
                        
                    if self.notif.render(True,"Reinicio","Usted quiere reiniciar la partida?"):
                        # self.retryGame()
                        print ("reinicio")

                if self.button_pause.x <= mouse_x <= self.button_pause.x + self.button_pause.img.get_width() and self.button_pause.y <= mouse_y <= self.button_pause.y + self.button_pause.img.get_height():    
                    self.notif.render(False,"Pausado","El juego esta pausado, toca nuevamente para seguir con la partida")
                    print("pause")