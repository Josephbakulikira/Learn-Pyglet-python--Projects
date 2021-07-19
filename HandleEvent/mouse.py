import pyglet
from pyglet.window import mouse

width, height = 800, 600
window = pyglet.window.Window(width, height, caption="mouse events")
# window.set_exclusive_mouse(True)
#window.set_mouse_visible(False)

# changing the mouse cursor
cursor = window.get_system_mouse_cursor(window.CURSOR_HAND)
window.set_mouse_cursor(cursor)

# load your image as cursor
# image = pyglet.image.load('cursor.png')
# cursor = pyglet.window.ImageMouseCursor(image, 16, 8)
# window.set_mouse_cursor(cursor)


# The x and y parameters give the coordinates of the mouse pointer,
# relative to the bottom-left corner of the window.
# The dx and dy parameters are for this purpose:
#  they give the distance the mouse travelled along each axis
#  to get to its present position.

# @window.event
# def on_mouse_motion(x, y, dx, dy):
#     print("mouse moved")

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('left button was clicked')
    elif button == mouse.RIGHT:
        print("Right button was clicked")
    elif button == mouse.MIDDLE:
        print("Middle button was clicked")
    print(modifiers)

@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("Left button was released")
    elif button == mouse.RIGHT:
        print("Right button was released")
    elif button == mouse.MIDDLE:
        print("Middle button was released")
@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    if button == mouse.LEFT:
        print(f"{dx},{dy}")





@window.event
def on_draw():
    window.clear()


pyglet.app.run()
