import pyglet
from cell import Cell

width, height = 500, 500
window = pyglet.window.Window(width, height)
cell = Cell(width//2, height//2, 100, 100)
cell.color = (255, 0, 0)
@window.event
def on_draw():
    window.clear()
    cell.draw()
pyglet.app.run()
