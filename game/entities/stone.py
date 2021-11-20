from ursina import *
from .voxel import Voxel
from ..textures import textures

class Stone(Voxel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.texture = textures["stone"]