import pyglet
from cell import Cell
from pyglet import clock
from pyglet.window import mouse, key
import random

width, height = 500, 500
white=(255, 255, 255)
window = pyglet.window.Window(width, height)

cell_size = 50
rows = height//cell_size
columns = width//cell_size

minefield = 20
options = []

class Mouse:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.left = False
        self.right = False
    def reset(self):
        m.left = False
        m.right = False

m = Mouse()

# generate Grid
Grid = [[None for _ in range(columns)] for i in range(rows)]
for x in range(rows):
    for y in range(columns):
        cell = Cell(x * cell_size, y*cell_size, cell_size-1, cell_size-1)
        #cell.color = white
        Grid[x][y] = cell
        options.append((x, y))

# set the mine cells
for i in range(minefield):
    choice = random.choice(options)
    options.remove(choice)
    x, y = choice
    Grid[x][y].isMine = True
# get the number of mines
for x in range(rows):
    for y in range(columns):
        Grid[x][y].countMines(Grid)

def Update(_dt):
    index_x, index_y = m.x//cell_size, m.y//cell_size
    if Grid[index_x][index_y] and m.left == True:
        Grid[index_x][index_y].activate(index_x, index_y, Grid)
    elif Grid[index_x][index_y] and m.right == True:
        Grid[index_x][index_y].activate(index_x, index_y, Grid,"RIGHT")

    for x in range(rows):
        for y in range(columns):
            Grid[x][y].update(m)

    m.reset()

@window.event
def on_mouse_press(x, y, button, modifiers):
    m.x, m.y = x, y
    if button == mouse.LEFT:
        m.left = True

    if button == mouse.RIGHT:
        m.right = True



@window.event
def on_draw():
    window.set_caption (f'FPS : {pyglet.clock.get_fps()}')
    window.clear()
    for x in range(rows):
        for y in range(columns):
            Grid[x][y].show()

clock.schedule_interval(Update, 1/30)


pyglet.app.run()
