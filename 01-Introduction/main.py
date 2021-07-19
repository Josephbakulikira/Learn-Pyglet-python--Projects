import pyglet

#width, height= 500, 500

# create window default
window = pyglet.window.Window(caption='initial caption')
#window.set_caption('A different caption')
#x, y = window.get_location()
#window.set_location(x + 800, y + 20)
#window.set_size(1280, 720)

# or by passing through your own width and height
# window = pyglet.window.Window(width, height)

# ---- visible parameter
#window = pyglet.window.Window(visible=False)
#window.set_visible()

# resizable windows
# window = pyglet.window.Window(resizable=True)
#
# window.set_minimum_size(320, 200)
# window.set_maximum_size(1024, 768)
# @window.event
# def on_resize(width, height):
#     print(f'{width},{height}')

# to get the window width , height
#print(f'{window.width}, {window.height}')

# main loop , add the event decorator
@window.event
def on_draw():
    # clear the screen
    window.clear()

# run the app
pyglet.app.run()
