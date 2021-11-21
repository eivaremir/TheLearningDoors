from ursina import *
from ..textures import textures

class Window(Button):
    def __init__(self, position: Vec3 = (3, 0, 0), size: int = 1, texture = textures["window"]) -> None:
        super().__init__(
            parent=scene,
            position=position,
            texture=texture,
            model='button',
            scale=Vec3(size, 5, .3),
        )