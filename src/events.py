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
        if self.event == pygame.KEYDOWN:
            pass

    def mouse (self,event : pygame) -> None:
        if self.event == pygame.MOUSEBUTTONDOWN:
            pass
