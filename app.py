from ursina.ursinastuff import destroy
from game import app

from ursina import color, held_keys

from game import hand
from game.entities.menu import Menu

menu = None
its_menuopen = False

def update():
    global menu, its_menuopen
    if held_keys['escape'] and not its_menuopen:
        menu = Menu() 
        print("Menu Abierto")
        its_menuopen= True
    elif held_keys['escape'] and its_menuopen:
        print("Menu Cerrado")
        its_menuopen= False
        destroy(menu)
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

if __name__ == "__main__":
    
    app.run()