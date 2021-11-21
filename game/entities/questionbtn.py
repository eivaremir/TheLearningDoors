from ursina import *
from ..config import CASTLE_WIDTH

well_done_sound = Audio('assets/sounds/Well_Done_1.mp3', loop=False, autoplay=False)
error_sound = Audio('assets/sounds/Error.mp3', loop=False, autoplay=False)

padding = .5
class QuestionBtn(Button):
    """
    QuestionBtn

    Example of usage:
    `questionbtn = QuestionBtn(event, position=(0, 0, 0), is_answer=True)`

    Parameters:
        event: function to be called when the button is clicked
        position: position of the button
        is_answer: if the button is an answer or not
    """

    def __init__(self, callback, img=None, text=None, position: Vec3 = (0, 0, 0), is_answer: bool = False) -> None:
        super().__init__(
            parent=scene,
            position=position,
            model ="cube",
            #scale = Vec3(1.5, 1,.2),
            texture=img,
            scale =  Vec3(CASTLE_WIDTH-1, padding,.05),
            text=text,
            color=color.white,
            text_color = color.black,
            text_origin=Vec3(0, 0, -1),
        )
        #self.tooltip = Tooltip('exit')

        self.callback = callback
        self.is_answer = is_answer

    def input(self, key: str) -> None:
        if self.hovered:
            
            if key == 'left mouse down' and self.is_answer:
                self.color = color.green
                self.highlight_color = color.green
                well_done_sound.play()
                self.callback(True)

            elif key == 'left mouse down' and not self.is_answer:
                self.color = color.red
                self.highlight_color = color.red
                error_sound.play()
                self.callback(False)