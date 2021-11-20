from game import app

from ursina import held_keys

from game import hand

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

if __name__ == "__main__":
    app.run()