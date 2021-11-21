from ursina import *
from .floor import Floor
from ..textures import textures

class StoneFloor(Floor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.texture = textures["stone"]