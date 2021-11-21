from ursina import *

class Menu(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            position = (0,0),
            color = rgb(2,2,2,a=200),
            scale = (3, 1),
            model = 'quad',
        )
        
class Exit(Button):
    def __init__(self):
        super().__init__(
            text = "Salir del Juego",
            text_color = color.black,
            scale = (0.2,0.1),
            position = (0,-0.12),
            color = color.brown 
        )
        
class PlayGame(Button):
    def __init__(self):
        super().__init__(
            text = "Volver al Juego",
            text_color = color.black,
            scale = (0.2,0.1),
            position = (0,0.12),
            color = color.green  
        )
