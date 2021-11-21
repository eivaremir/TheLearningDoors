from ursina import vec3
from .levels import get_questions
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

from .textures import textures
from .entities.voxel import Voxel
from .entities.grass import Grass
from .entities.castle import Castle
from .entities.brick import Brick
from .entities.timer import Timer
from .entities.window import Window

from .config import Z_LIMITS 
from .config import X_LIMITS 
from .config import CASTLE_DEPTH
from .config import MAX_LEVELS 
import random
from .entities.hand import Hand
import json
from .levels import levels

from zipfile import ZipFile
  


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=textures['sky'],
            scale=150,
            double_sided=True
        )


Entity(model = "quad", texture= "assets/descarga.png", position = (-3, 3, CASTLE_DEPTH *-1 -1), scale = Vec3(3.5,2,2) )

sky = Sky()

for z in range(Z_LIMITS[0], Z_LIMITS[1]+1):
    for x in range(X_LIMITS[0], X_LIMITS[1]+1):
        voxel = Grass(position=(x, 0, z))
        is_delimited_region = (abs(z) == Z_LIMITS[1] or abs(x) == X_LIMITS[1])
        if is_delimited_region:
            for y in range(1, 2):
                voxel = Brick(position=(x, y, z))

#Generate the castle with the levels
#castle = Castle(levels=get_questions())

f= open("data.json").readlines()[0]
l =json.loads(f)[0:MAX_LEVELS]
random.shuffle(l)

# specifying the zip file name
"""file_name = "questions0.zip"
  
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
  
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall(path="./game/assets")
    print('Done!')  

#f= open("data.json").readlines()[0]
f= open("./game/assets/questions2/questions.json","w+").readlines()[0]
l =json.loads(f)
print(l)"""
castle = Castle(levels= l)


#player.rotation_y = -95

seconds = 5

timer = Timer(seconds=6)
timer.start()


player = FirstPersonController()
#Set the player to the starting position
player.set_position([0, 25, -7])
hand = Hand()



