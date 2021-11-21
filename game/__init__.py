from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

from .textures import textures
from .entities.voxel import Voxel
from .entities.grass import Grass
from .entities.castle import Castle
from .entities.brick import Brick
from .entities.timer import Timer


from .config import Z_LIMITS 
from .config import X_LIMITS 

from .entities.hand import Hand

from .levels import levels
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
        is_delimited_region = (abs(z) == Z_LIMITS[1] or abs(x) ==  X_LIMITS[1])
        if is_delimited_region:
            for y in range(1,4):
                voxel = Brick(position=(x,y,z))

#Generate the castle with the levels
castle = Castle(levels=levels)

#Set the player to the starting position
player.set_position([0,2,-10])

player.rotation_y = -95

timer = Timer()


hand = Hand()

