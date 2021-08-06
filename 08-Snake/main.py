import pyglet
from pyglet import shapes, clock
from pyglet.window import key
from random import randrange

width, height = 600, 600
window = pyglet.window.Window(width=width, height=height)

score = pyglet.text.Label('0',
    x = 30,
    y = height-30,
    anchor_x='center',
    anchor_y='center',
    font_size=18,
    font_name="Verdana",
    bold=True)

gameisOverText = pyglet.text.Label('Game Over - Press ENTER to restart ',
    x = width//2,
    y = height//2,
    anchor_x='center',
    anchor_y='center',
    font_size=20,
    font_name="Times New Roman",
    bold=True)

score.color = (255, 255, 255, 150)

speed = 120
direction = 'RIGHT'
gameIsOver = False

snake_size = 20
initial_size = 5
newFood = True
snake = []

snakeColor = (55, 255, 160)
foodColor = (230, 30, 40)

# initial position of the snake
pos = [width//2, height//2]
# body of the snake
body = [[ pos[0]-i * snake_size, pos[1]] for i in range(initial_size)]

# spawn new random food
def spawnFood():
    return [randrange(1, width//snake_size) * snake_size , randrange(1, height//snake_size) * snake_size]

def Reset():
    global food, newFood, score, direction, gameisOver, pos, body
    direction = "RIGHT"
    score.text = "0"
    food = spawnFood()
    pos = [width//2, height//2]
    body = [[ pos[0]-i * snake_size, pos[1]] for i in range(initial_size)]


food = spawnFood()

def update(dt):
    if gameIsOver:
        Reset()
    return

@window.event
def on_key_press(symbol, modifiers):
    global direction, gameIsOver
    if symbol == key.UP or symbol == key.W:
        if direction != "DOWN":
            direction = "UP"
    elif symbol == key.DOWN or symbol == key.S:
        if direction != "UP":
            direction = "DOWN"
    elif symbol == key.RIGHT or symbol == key.D:
        if direction != "LEFT":
            direction = "RIGHT"
    elif symbol == key.LEFT or symbol == key.A:
        if direction != "RIGHT":
            direction = "LEFT"
    elif symbol == key.RETURN or symbol == key.ENTER:
        gameIsOver = False


@window.event
def on_draw():
    global food, newFood, gameIsOver
    window.set_caption (f' SNAKE ( FPS : {pyglet.clock.get_fps()} )')

    if gameIsOver != True:
        window.clear()

        if direction == "UP":
            pos[1] += snake_size
        elif direction == "DOWN":
            pos[1] -= snake_size
        elif direction == "RIGHT":
            pos[0] += snake_size
        elif direction == "LEFT":
            pos[0] -= snake_size

        body.insert(0, list(pos))
        if pos[0] == food[0] and pos[1] == food[1]:
            score.text = str(int(score.text) + 1)
            newFood = False
        else:
            body.pop()

        if not newFood:
            food = spawnFood()

        newFood = True
        for position in body:
            shapes.Rectangle(x=position[0] , y=position[1], width=snake_size, height=snake_size, color=snakeColor).draw()
        shapes.Rectangle(x=food[0] , y=food[1], width=snake_size, height=snake_size, color=foodColor).draw()

        # check if the game is over

        for part in body[1:]: # checking if the snake collide with itself
            if pos[0] == part[0] and pos[1] == part[1]:
                gameIsOver = True
        # constraint
        if pos[0] < 0 or pos[0] > width-snake_size or pos[1] < 0 or pos[1] > height-snake_size:
            gameIsOver = True

        score.draw()
    else:
        gameisOverText.draw()


clock.schedule_interval(update, 1/10.)
pyglet.app.run()
