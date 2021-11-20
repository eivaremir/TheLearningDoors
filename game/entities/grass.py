from ursina import *
from voxel import Voxel

class Grass(Voxel):
    def __init__(self, position = (0,0,0)):
        super().__init__()