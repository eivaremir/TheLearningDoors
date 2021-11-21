from ursina import *


from .questionbtn import QuestionBtn, padding
from .stone import Stone
from .brick import Brick
from .floor import Floor
from .door import Door
from .congrats import Congrats
from .initbtn import InitButton
from ..config import Z_LIMITS
from ..config import X_LIMITS
from ..config import LEVELS_SIZE
from ..config import CASTLE_WIDTH
from ..textures import textures
import threading
import time


well_done_sound = Audio('assets/sounds/Well_Done_1.mp3', loop=False, autoplay=False)

class Castle():

    WIDTH = CASTLE_WIDTH
    DEPTH = 4
    current_player_level = 0

    def __init__(self,levels = [1,2,3,4,5,6]):
        self.levels = levels
        self.HEIGHT = len(levels) * LEVELS_SIZE +1
        for z in range(self.DEPTH * -1,self.DEPTH +1 ):
            for x in range(self.WIDTH * -1 ,self.WIDTH + 1):
                for y in range(1,self.HEIGHT + self.HEIGHT*2):
                    is_delimited_region = (abs(z) == self.DEPTH or abs(x) == self.WIDTH)
                    is_the_door =  (y<= 3 and x>=0 and x<=1 and z == self.DEPTH * -1)
                    if is_delimited_region and not is_the_door:
                        if y > LEVELS_SIZE and ((y+1) % (LEVELS_SIZE/2) == 0 ) :
                            Entity(model = "quad", texture=textures["window"], position = (x,y-.2,z))
                            
                            
                        else:
                            stone = Stone(position=(x,y,z))
                    if x==1 and y==1 and z==self.DEPTH * -1:
                        door = Door(position=(.5,y,z),size = 2)

                    if y% LEVELS_SIZE == 0:
                        stone = Stone(position=(x,y,z))

                    

        l = 1              
        for level in levels:
            self.generate_level(level,l)
            l+=1

        self.generate_entrance()
        self.generate_start_game()
        self.generate_congrats()

    def upgrade_level(self,delay=1.7):
        from .. import player 
        self.current_player_level +=1
        
        def move_player(delay):

            time.sleep(delay)
            player.set_position([0,player.y+LEVELS_SIZE,0])

        thread = threading.Thread(target=move_player,args=(delay,))
        thread.start()
    def generate_congrats(self):
        c = Congrats(len(self.levels))
    def generate_level(self,level,l):
        a = 1
        delta = (LEVELS_SIZE -1) / len(level["answers"])
        delta_y = l * LEVELS_SIZE # - delta
        for answer in level["answers"]:

            qb = QuestionBtn(
                lambda x :  self.upgrade_level() if x else None ,
                text=answer["value"],
                position = Vec3((CASTLE_WIDTH-1) / 2, (LEVELS_SIZE-1)+ delta_y,self.DEPTH-.6),is_answer=answer.get("answer",False))
                #position = Vec3(0,5,0),is_answer=True)
            delta_y = delta_y - delta
            a+=1

    def generate_start_game(self):
        btn = InitButton(self.upgrade_level)
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