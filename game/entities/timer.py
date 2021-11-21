from ursina import *

import threading
import time


class Timer(Text):
    
    def __init__(self,callback=None,seconds=5):
        super().__init__(
        
            text = str(seconds),
            position = (0.60,0.47), 
            background= True,
            
        )
        self.seconds=seconds
        self.callback = callback
        
        # thread self.update
    def updateTimer(self):
        
        while self.seconds:
            print(self.seconds,"---",self.text)
            self.text = str(self.seconds)
            time.sleep(1)
            self.seconds = self.seconds-1
        #self.callback(False)      
            
    def start(self):
        thread = threading.Thread(target=self.updateTimer)
        thread.start()
        
                
   
            
    """
        while 60 
        secons--
        self text = .....
        
        
        """