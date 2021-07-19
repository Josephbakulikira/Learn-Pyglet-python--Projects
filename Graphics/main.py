import pyglet
from pyglet import shapes

width, height = 1000, 1000
window = pyglet.window.Window(width, height)

# shapes
circle = shapes.Circle(x=width//2, y = height//2, radius=100, color=(255, 255, 0))
rect = shapes.Rectangle(x=400, y=400, width=200, height=130, color=(0, 0, 255))

rect.opacity = 150
rect.rotation = 45
#shape properties:
# anchor_x, anchor_y, anchor_position, rotation
@window.event
def on_draw():
    window.clear()
    # pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
    #     ('v2i', (width//2, height//2)),
    #     ('c3B', (1, 255, 1))
    # )
    circle.draw()
    rect.draw()

pyglet.app.run()
