import pyglet
from pyglet import shapes
from pyglet.window import key, mouse

# setup
width, height = 800, 800
window = pyglet.window.Window(width, height)

#global variables

white = (255, 255, 255)
black = (0, 0, 0, 255)
green = (80,203,147, 255)
cell_size = 200
t = 4
Xoffset = 100
Yoffset = 100

turn = pyglet.text.Label(
"X",
x=width//2,
y=50,
anchor_x='center', anchor_y='center',
font_size=35,
font_name="Verdana",
)

Winner = pyglet.text.Label(
"",
x=width//2,
y=height-50,
anchor_x='center', anchor_y='center',
font_size=35,
font_name="Verdana",
color=green
)

Board = [[None for _ in range(3)] for i in range(3)]
Cells = []

for x in range(3):
    for y in range(3):

        cell = shapes.Rectangle(x=x*cell_size+Xoffset, y=y*cell_size+Yoffset, width=cell_size-t, height=cell_size-t, color=white)

        text = pyglet.text.Label(
        "",
        x=x*cell_size+Xoffset + cell_size//2,
        y=y*cell_size+Yoffset + cell_size//2,
        anchor_x='center', anchor_y='center',
        font_size=100,
        font_name="Arial",
        bold=True

        )
        text.color = black
        Board[x][y] = text
        Cells.append(cell)

def CheckWin():
    # check for winning columns
    for x in range(3):
        if Board[x][0].text == Board[x][1].text == Board[x][2].text and Board[x][0].text != "":
            Board[x][0].color = green
            Board[x][1].color = green
            Board[x][2].color = green

            Winner.text = turn.text + " is the winner !"
            return
    # check for winning rows
    for y in range(3):
        if Board[0][y].text == Board[1][y].text == Board[2][y].text and Board[0][y].text != "":
            Board[0][y].color = green
            Board[1][y].color = green
            Board[2][y].color = green

            Winner.text = turn.text + " is the winner !"
            return

    # check for winning diagonal
    if Board[0][0].text == Board[1][1].text == Board[2][2].text and Board[0][0].text != "":
        Board[0][0].color = green
        Board[1][1].color = green
        Board[2][2].color = green

        Winner.text = turn.text + " is the winner !"
        return
    if Board[0][2].text == Board[1][1].text == Board[2][0].text and Board[0][2].text != "":
        Board[0][2].color = green
        Board[1][1].color = green
        Board[2][0].color = green
        Winner.text = turn.text + " is the winner !"
        return

def Restart():
    for x in range(3):
        for y in range(3):
            Board[x][y].text = ""
            Board[x][y].color = black
    Winner.text = ""

@window.event
def on_key_press(symbol, modifier):
    # press space to Restart
    if symbol == key.SPACE:
        Restart()
        turn.text = "X"

@window.event
def on_mouse_press(x, y, button, modifier):
    if button == mouse.LEFT:
        if x > Xoffset and y > Yoffset and x < width-Xoffset and y < height-Yoffset:
            # get the cell index
            x_index = ( (x+Xoffset) // cell_size ) - 1
            y_index = ( (y+Yoffset) // cell_size ) - 1
            # check if the cell is occupied or not
            if Board[x_index][y_index].text == "":
                Board[x_index][y_index].text = turn.text
                CheckWin()
                turn.text = "O" if turn.text=="X" else "X"

@window.event
def on_draw():
    window.clear()
    for cell in Cells:
        cell.draw()
    for x in range(3):
        for y in range(3):
            Board[x][y].draw()
    Winner.draw()
    turn.draw()
pyglet.app.run()
