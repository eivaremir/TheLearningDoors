from ursina import *

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
    def __init__(self, callback: function, position: Vec3 = (0, 0, 0), is_answer: bool = False) -> None:
        super().__init__(
            parent=scene,
            position=position,
            model='white_cube',
            scale=Vec3(1, 1, 1),
            color=color.white
        )
        self.callback = callback
        self.is_answer = is_answer

    def input(self, key: str) -> None:
        if self.hovered:
            if key == 'left mouse down' and self.is_answer:
                self.color = color.green
                self.callback(True)

            elif key == 'left mouse down' and not self.is_answer:
                self.color = color.red
                self.callback(False)