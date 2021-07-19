import pyglet
from pyglet.window import key

window = pyglet.window.Window()

# Unlike the corresponding key symbols,
# it is not possible to determine whether
# the left or right modifier is held down
# (though you could emulate this behaviour by keeping track of the key states yourself).


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        print("space button was pressed")
    if modifiers & key.MOD_SHIFT:
        print("Shift button")


@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.A:
        print("the A key was released")
    pass

# text button
# @window.event
# def on_text(text):
#     print(text)

keys = key.KeyStateHandler()
window.push_handlers(keys)

@window.event
def on_draw():
    window.clear()
    if  keys[key.RETURN]:
        print("Enter (Return) key")

pyglet.app.run()
