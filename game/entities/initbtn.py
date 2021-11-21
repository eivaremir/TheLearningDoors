from ursina import *
from ..config import CASTLE_WIDTH
from ..config import LEVELS_SIZE
from ..config import CASTLE_DEPTH

well_done_sound = Audio('assets/sounds/Well_Done_1.mp3', loop=False, autoplay=False)
error_sound = Audio('assets/sounds/Error.mp3', loop=False, autoplay=False)

padding = .5
class InitButton(Button):
    def __init__(self,callback):
        super().__init__(
            parent=scene,
            position=Vec3(0,LEVELS_SIZE / 2,CASTLE_DEPTH-.5),
            model ="cube",
            scale =  Vec3(CASTLE_WIDTH*1.5,2,.05),
            text="Presiona aquí para iniciar",
            color=color.azure,
            text_origin=Vec3(0, 0,-1)
        )
        self.callback = callback
    def input(self, key: str) -> None:
        if self.hovered:
            
            if key == 'left mouse down':
                self.color = color.green
                well_done_sound.play()
                self.callback(1)
                