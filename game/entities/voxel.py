from ursina import *
from ..textures import textures

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = textures["grass"]):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = .5,
            texture =texture,
            color = color.color(0,0,random.uniform(.9,1)),
            scale = .5
        )