import pyglet
from pyglet import shapes

class Cell(shapes.Rectangle):
    def __init__(self):
        super(Cell, self).__init__(x, y, w, h)
        self.x = x
        self.y = y
        self.width = w
        self.height = h
