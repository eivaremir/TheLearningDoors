from ursina import *
from ..config import CASTLE_WIDTH
from ..config import LEVELS_SIZE
from ..config import CASTLE_DEPTH


class Congrats(Button):
    def __init__(self,levels,callback=None):
        super().__init__(
            parent=scene,
            position=Vec3(0,(LEVELS_SIZE *(levels+1)) + (LEVELS_SIZE/2),CASTLE_DEPTH-.5),
            model ="cube",
            scale =  Vec3(CASTLE_WIDTH*2,LEVELS_SIZE,.05),
            text="Felicidades, has culminado con éxito",
            color=color.gold,
            text_origin=Vec3(0, 0,-1),
            highlight_color = color.gold,
        )
        self.callback = callback
    def input(self, key: str) -> None:
        if self.hovered:
            
            if key == 'left mouse down':
                self.color = color.green
                #well_done_sound.play()
                #self.callback(1)
                