import pyglet
from pyglet import shapes

width, height = 1000, 1000
window = pyglet.window.Window(width, height)

batch = pyglet.graphics.Batch()
# shapes

# Circle(x, y, radius, segments=None, color=(255, 255, 255), batch=None, group=None)
circle = shapes.Circle(x=width//2, y = height//2, radius=100, color=(255, 255, 0), batch=batch)

# Rectangle(x, y, width, height, color=(255, 255, 255), batch=None, group=None)
rect = shapes.Rectangle(x=400, y=400, width=200, height=130, color=(0, 0, 255), batch=batch)

# BorderedRectangle(x, y, width, height, border=1, color=(255, 255, 255), border_color=(100, 100, 100), batch=None, group=None)
rect2 = shapes.BorderedRectangle(700, 700, 200, 200, border=30, color=(255, 255, 255), border_color=(100, 100, 100), batch=batch)

# Line(x, y, x2, y2, width=1, color=(255, 255, 255), batch=None, group=None)
line = shapes.Line(200, 800, 800, 200, 5, (0, 255, 134), batch=batch)


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
    # circle.draw()
    # rect.draw()
    # rect2.draw()
    # line.draw()
    batch.draw()

pyglet.app.run()
