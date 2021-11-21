from ursina import *
from ..config import CASTLE_WIDTH

padding = .5


class Question(Button):
    """
    Question

    Example of usage:
    `question = Question(position=(0, 0, 0))`

    Parameters:
        position: position of the question
    """

    def __init__(self, text=None, img=None, position: Vec3 = (0, 0, 0)) -> None:
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            scale=Vec3(1, 1, 1),
            texture=img,
            color=color.white,
            text=text,
            text_origin=Vec3(0, 0, -1),
            highlight_color=color.white
        )
