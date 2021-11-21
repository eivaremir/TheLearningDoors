from ursina import *
from ..textures import textures
door_open_sound = Audio('assets/sounds/DoorOpen.mp3', loop=False, autoplay=False)
door_close_sound = Audio('assets/sounds/DoorClose.mp3', loop=False, autoplay=False)

class Door(Button):
    """
    Door is a button that opens and closes.

    Example of usage:
    `door = Door(position=(0, 0, 0), size=2)`
    """
    def __init__(self, position: Vec3 = (0, 0, 0), size: int = 1) -> None:
        super().__init__(
            parent=scene,
            position=position,
            texture=textures["door"],
            model='cube',
            scale=Vec3(size, 5, .3),
            color=rgb(135, 62, 35),
        )
        self.initial_position = self.position
        self.open = False
        self.scale = Vec3(size, 5, .3)

    def input(self, key: str) -> None:
        if self.hovered:
            if key == 'left mouse down' and not self.open:
                # open door
                print('open')
                self.open = True
                self.rotation = Vec3(0, -90, 0)
                self.position = Vec3(
                    self.initial_position.x + self.scale.x / 2,
                    self.initial_position.y,
                    self.initial_position.z + self.scale.x / 2)
                door_open_sound.play()

            elif key == 'left mouse down' and self.open:
                # close door
                self.open = False
                self.rotation = Vec3(0, 0, 0)
                self.position = self.initial_position
                door_close_sound.play()