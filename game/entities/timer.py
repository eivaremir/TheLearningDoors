from ursina import *

class Timer(Text):
    def __init__(self):
        super().__init__(
            text = "hola, soy timer",
            position = (0.60,0.47), 
            background= True
        )