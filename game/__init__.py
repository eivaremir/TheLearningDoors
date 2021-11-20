from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

from .textures import textures
from .entities.voxel import Voxel

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = textures['sky'],
            scale = 150,
            double_sided = True
        )


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))
        

player = FirstPersonController()
sky = Sky()

