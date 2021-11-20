from ursina import *
from .voxel import Voxel
from ..textures import textures

class Dirt(Voxel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.texture = textures["dirt"]