from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController





app = Ursina()

from .textures import textures
from .entities.voxel import Voxel
from .entities.grass import Grass
from .entities.castle import Castle
from .entities.brick import Brick


from .config import Z_LIMITS 
from .config import X_LIMITS 

from .entities.hand import Hand

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = textures['sky'],
            scale = 150,
            double_sided = True
        )



        

player = FirstPersonController()
sky = Sky()

for z in range(Z_LIMITS[0],Z_LIMITS[1]+1):
    for x in range(X_LIMITS[0],X_LIMITS[1]+1):
        voxel = Grass(position=(x,0,z))

        
castle = Castle()

player.set_position([0,0,-10])



hand = Hand()
