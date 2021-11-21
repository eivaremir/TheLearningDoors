from ursina import *


class Hand(Entity):
    """
    Hand is a child of the camera.ui entity, which is a child of the camera entity.

    Usage:
    `hand = Hand()`
    """
    def __init__(self):
        super().__init__(parent=camera.ui,
                         model='assets/arm',
                         texture='assets/arm_texture',
                         scale=0.2,
                         rotation=Vec3(150, -10, 0),
                         position=Vec2(0.4, -0.6))

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)