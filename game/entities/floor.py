from ursina import *
from .voxel import Voxel
from ..textures import textures

class Floor(Voxel):
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        self.texture = textures["brick"]
        self.scale = Vec3(1,.1,1)