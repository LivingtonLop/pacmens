from config.envioriment_to_class import (
                                            json,
                                            os,
                                            Union,
                                            load_dotenv
                                        )

load_dotenv()

class ResourcesToClass():
    
    def __init__(self) -> None:
        self.to_execute : bool = True
        self.to_pause : bool = False

        #surface or window or screen
        self.surface_name : str= self.getDataEnviorimentValue("APP_NAME", "NO NAME")

        self.surface_width : int = self.getDataEnviorimentValue("SURFACE_WITDH",1000)
        self.surface_height : int = self.getDataEnviorimentValue("SURFACE_HEIGHT",600)




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
        
        