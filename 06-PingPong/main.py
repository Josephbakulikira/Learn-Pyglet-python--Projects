import pyglet
from pyglet import shapes, clock
from pyglet.window import key
import math
from random import uniform

white = (255, 255, 255)
width, height = 1400, 800
offset = 10
speed = 200
window = pyglet.window.Window(width, height)

hitSound = pyglet.media.load("pop.mp3")

angle = 0
val = math.pi/4

# creating a batch
batch = pyglet.graphics.Batch()

leftScore = pyglet.text.Label("0", x=100, y=height-50, anchor_x='center', anchor_y='center',
font_size=50,
font_name="Verdana",
bold=True,
batch=batch
)

rightScore = pyglet.text.Label("0", x=width-100, y=height-50, anchor_x='center', anchor_y='center',
font_size=50,
font_name="Verdana",
bold=True,
batch=batch)


#initialize shapes
Line = shapes.Line(width//2, 0, width//2,height, 6, color = white,
batch=batch)
Line.opacity = 200

Ball = shapes.Circle(x=width//2, y = height//2, radius=20, color=white,
batch=batch)
Ball.velocity = [0, 0]

leftPaddle = shapes.Rectangle(
x = offset,
y = height//2,
width=30,
height=150,
color=white,
batch=batch
)
leftPaddle.anchor_y = leftPaddle.height//2
leftPaddle.move = 0 # velocity

rightPaddle = shapes.Rectangle(
x = width-offset,
y = height//2,
width=30,
height=150,
color=white,
batch=batch
)

rightPaddle.anchor_y = rightPaddle.height//2
rightPaddle.anchor_x = rightPaddle.width
rightPaddle.move = 0 # velocity

def translateValue(value, min1, max1, min2, max2):
    return min2 + (max2 - min2)* ((value-min1)/(max1-min1))

# check if the ball hit the paddles or not

def CheckLeftPaddle():
    if (Ball.y - Ball.radius < leftPaddle.y + leftPaddle.height//2 and
       Ball.y + Ball.radius > leftPaddle.y - leftPaddle.height//2 and
       Ball.x - Ball.radius < leftPaddle.x + leftPaddle.width) :
       if Ball.x > leftPaddle.x:
           diff = Ball.y - (leftPaddle.y - leftPaddle.height//2)
           # map the range 0->height to -45 -> 45
           angle = translateValue(diff, 0, leftPaddle.height, -val, val)
           # using the polar cordinnate
           Ball.velocity[0] = 10 * math.cos(angle)
           Ball.velocity[1] = 10 * math.sin(angle)
           Ball.x = leftPaddle.x + leftPaddle.width + Ball.radius

def CheckRightPaddle():
    if (Ball.y - Ball.radius < rightPaddle.y + rightPaddle.height//2 and
       Ball.y + Ball.radius > rightPaddle.y - rightPaddle.height//2 and
       Ball.x + Ball.radius > rightPaddle.x - rightPaddle.width):
       if Ball.x < rightPaddle.x:
           diff = Ball.y - (rightPaddle.y - rightPaddle.height//2)
           # map the range 0->height to 225 to 135
           angle = translateValue(diff, 0, rightPaddle.height, math.radians(225), math.radians(135))
           # using the polar cordinnate
           Ball.velocity[0] = 10 * math.cos(angle)
           Ball.velocity[1] = 10 * math.sin(angle)
           Ball.x = rightPaddle.x - rightPaddle.width - Ball.radius

# check if the ball is out of bound
def Boundary():
    if Ball.y < Ball.radius or Ball.y > height-(Ball.radius):
        # reflect the velocity vector of the ball
        Ball.velocity[1] *= -1

    if Ball.x  > width - (Ball.radius//2):
        #print(f"here right: {Ball.x}")
        leftScore.text = str(int(leftScore.text)+1)
        hitSound.play()

        reset()

    if Ball.x < Ball.radius:
        #print(f"here left: {Ball.x}")
        rightScore.text = str(int(rightScore.text)+1)
        hitSound.play()
        reset()

def reset():
    Ball.x = width//2
    Ball.y = height//2
    angle = uniform(-val, val)
    Ball.velocity[0] = 10 * math.cos(angle)
    Ball.velocity[1] = 10 * math.sin(angle)

    if uniform(0, 1) < 0.5:
        Ball.velocity[0] *= -1

reset()
def update(dt):
    #update paddle positions
    leftPaddle.y += leftPaddle.move * dt
    rightPaddle.y += rightPaddle.move * dt

    CheckLeftPaddle()
    CheckRightPaddle()
    Boundary()


    #update Ball position
    Ball.x += Ball.velocity[0]
    Ball.y += Ball.velocity[1]

    # constraint
    if leftPaddle.y < leftPaddle.height//2:
        leftPaddle.y = leftPaddle.height//2
    elif leftPaddle.y > height-leftPaddle.height//2:
        leftPaddle.y = height-leftPaddle.height//2

    if rightPaddle.y < rightPaddle.height//2:
        rightPaddle.y = rightPaddle.height//2
    elif rightPaddle.y > height-rightPaddle.height//2:
        rightPaddle.y = height-rightPaddle.height//2

@window.event
def on_key_press(symbol, modifier):
    if symbol == key.UP:
        # up arrow is pressed
        rightPaddle.move = speed
    elif symbol == key.DOWN:
        # down arrow is pressed
        rightPaddle.move = -speed

    if symbol == key.W:
        # 'w' key is pressed
        leftPaddle.move = speed
    elif symbol == key.S:
        # 'S' key is pressed
        leftPaddle.move = -speed


@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        # up arrow is pressed
        rightPaddle.move = 0
    elif symbol == key.DOWN:
        # down arrow is pressed
        rightPaddle.move = 0

    if symbol == key.W:
        # 'w' key is pressed
        leftPaddle.move = 0
    elif symbol == key.S:
        # 'S' key is pressed
        leftPaddle.move = 0
clock.schedule_interval(update, 1/60.)

@window.event
def on_draw():
    window.clear()
    clock.tick(60)
    window.set_caption (f'FPS : {pyglet.clock.get_fps()}')

    # leftScore.draw()
    # rightScore.draw()
    # Line.draw()
    # leftPaddle.draw()
    # rightPaddle.draw()

    batch.draw()
    Ball.draw()

pyglet.app.run()
