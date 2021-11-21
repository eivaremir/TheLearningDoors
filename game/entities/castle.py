from ursina import *

from game.entities.voxel import Voxel
from .stone import Stone
from .brick import Brick
from .floor import Floor
from .door import Door
from ..config import Z_LIMITS
from ..config import X_LIMITS
from ..config import LEVELS_SIZE

class Castle():

    WIDTH = 7
    DEPTH = 4
    
    def __init__(self,levels = [1,2,3,4,5,6]):
        self.HEIGHT = len(levels) * LEVELS_SIZE
        for z in range(self.DEPTH * -1,self.DEPTH +1 ):
            for x in range(self.WIDTH * -1 ,self.WIDTH + 1):
                for y in range(1,self.HEIGHT +1):
                    is_delimited_region = (abs(z) == self.DEPTH or abs(x) == self.WIDTH)
                    is_the_door =  (y<= 3 and x>=0 and x<=1 and z == self.DEPTH * -1)
                    if is_delimited_region and not is_the_door:
                        #pass
                        stone = Stone(position=(x,y,z))
                        #else:
                        #    stone = Stone(position=(x,y,z))
                    if x==1 and y==1 and z==self.DEPTH * -1:
                        door = Door(position=(.5,y,z),size = 2)

                    if y% LEVELS_SIZE == 0:
                        stone = Stone(position=(x,y,z))
                    
        

        self.generate_entrance()

    def generate_entrance(self):

        for z in range(Z_LIMITS[0],Z_LIMITS[1]+1):
            for x in range(X_LIMITS[0],X_LIMITS[1]+1):
                # if its infront of the castle
                # andits in the center of the castle
                if z < self.DEPTH * -1 and z > Z_LIMITS[0]*.8 \
                    and x>=X_LIMITS[0]*.05 and x<=X_LIMITS[1]*.05:
                    pass
                    #destroy(voxel)
                    voxel = Floor(position=(x,0,z))