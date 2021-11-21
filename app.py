from ursina.application import pause, resume
from ursina.ursinastuff import destroy
from game import app
from ursina import *

from game import hand
from game.entities.menu import Menu, Exit, PlayGame

#from game.__init__ import voxel


its_menuopen = False



menu = None
exit = None
play = None

def update():
    global menu, its_menuopen,exit,play
    if held_keys['escape'] and not its_menuopen:
        mouse.visible = True
        mouse.locked = False
        window.exit_button.visible = True
        pause()
        menu = Menu()
        exit = Exit()
        play = PlayGame()
        
        exit.on_click = application.quit
        
        def restart():
            mouse.visible = False
            mouse.locked = True
            window.exit_button.visible = False
            destroy(menu)
            destroy(exit)
            destroy(play)
            resume()
        play.on_click = restart
        
        print("Menu Abierto")
        its_menuopen= True
        
    elif held_keys['escape'] and its_menuopen:
        print("Menu Cerrado")
        its_menuopen= False
        menu = None
        exit = None
        play = None
            
        
        
        
        
        
        
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

if __name__ == "__main__":
    
    app.run()