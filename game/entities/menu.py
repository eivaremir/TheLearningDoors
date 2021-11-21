from ursina import *

class Menu(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            position = Vec3(0,0,0),
            background = "./assets/Door.png",
            scale = (.8, .8),
            model = 'quad',)
