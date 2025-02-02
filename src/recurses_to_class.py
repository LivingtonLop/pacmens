from map import Map
from entity import Entity
from buttons import Button
from notif import Notif
from config.envioriment_to_class import (
                                            json,
                                            os,
                                            Union,
                                            pygame,
                                            load_dotenv,
                                            BTN_PAUSE_X,BTN_PAUSE_y,
                                            BTN_RETRY_X,BTN_RETRY_y
                                        )

load_dotenv()
class ResourcesToClass():
    
    def __init__(self) -> None:
        
        self.resetExcute()

    @staticmethod
    def getDataonJSON(dir_filename: str) -> dict | None:
        file_json = dir_filename
        
        data : dict = None

        try:

            with open(file_json, 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            print(f"Error: El archivo {file_json} no existe.")
        except json.JSONDecodeError:
            print(f"Error: El archivo {file_json} no contiene un JSON válido.")
        except KeyError as e:
            print(f"Error: Falta la clave {e} en los datos del archivo JSON.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        return data
    
    @staticmethod
    def getDataEnviorimentValue(name_value:str, default: Union[str,int,bool,None] = None) -> Union[str,int,bool,None]:
        data = os.getenv(key=name_value,default=default)

        if data is None:
            return default
        if data.lower() in ['true','false']:
            return data.lower() == 'true'
        if data.isdigit():
            return int(data)
        
        return data 
        
    def setPause(self):
        self.to_pause = not self.to_pause
        self.button_pause.setImg(self.getDataEnviorimentValue(name_value="DIR_IMAGE_BUTTON_TO_CONTINUE" if self.to_pause else "DIR_IMAGE_BUTTON_TO_PAUSE"))

    def resetExcute(self):
        self.kill_player : bool = False
        self.to_execute : bool = True
        self.to_pause : bool = False
        #surface or window or screen
        self.surface_name : str= self.getDataEnviorimentValue("APP_NAME", "NO NAME")

        self.surface_width : int = self.getDataEnviorimentValue("SURFACE_WITDH",1000)
        self.surface_height : int = self.getDataEnviorimentValue("SURFACE_HEIGHT",600)

        self.level_now : int = 1 #default
        self.map = Map(self.getDataonJSON(dir_filename=f"{self.getDataEnviorimentValue(name_value="DIR_MAPS")}/level_{self.level_now}.json"))

        self.pacman = Entity([
            self.getDataEnviorimentValue(name_value="DIR_IMAGE_SPRITE_PACMAN"),
            self.getDataEnviorimentValue(name_value="DIR_IMAGE_SPRITE_PACMAN2")
        ],100,35,(20,20))
        self.enemies_blue = Entity([self.getDataEnviorimentValue(name_value="DIR_IMAGE_SPRITE_PHANTOM_BLUE")],200,35, (20,20),True)
        self.enemies_pink = Entity([self.getDataEnviorimentValue(name_value="DIR_IMAGE_SPRITE_PHANTOM_PINK")],400,35, (20,20),True)
        self.enemies_red = Entity([self.getDataEnviorimentValue(name_value="DIR_IMAGE_SPRITE_PHANTOM_RED")],300,35, (20,20),True)
        self.enemies_yellow = Entity([self.getDataEnviorimentValue(name_value="DIR_IMAGE_SPRITE_PHANTOM_YELLOW")],500,35, (20,20),True)

        self.other_entities : list = [self.enemies_blue,self.enemies_pink,self.enemies_red,self.enemies_yellow]

        self.button_pause = Button(BTN_PAUSE_X, BTN_PAUSE_y, self.getDataEnviorimentValue(name_value="DIR_IMAGE_BUTTON_TO_PAUSE"))
        self.button_retry = Button(BTN_RETRY_X, BTN_RETRY_y, self.getDataEnviorimentValue(name_value="DIR_IMAGE_BUTTON_TO_RETRY"))

        self.notif = Notif()

        self.all_sprite_pacman = pygame.sprite.Group()
        self.all_sprite_pacman.add(self.pacman)

        self.image_coin = pygame.image.load(self.getDataEnviorimentValue(name_value="DIR_IMAGE_SKIN_TO_ITEM_COIN"))
        self.image_apple = pygame.image.load(self.getDataEnviorimentValue(name_value="DIR_IMAGE_SKIN_TO_ITEM_APPLE"))
        