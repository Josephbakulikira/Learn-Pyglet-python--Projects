import pyglet
from pyglet.image.codecs.png import PNGImageDecoder

width, height = 1000, 1000
window = pyglet.window.Window(width, height)


# ------ Text --------------

HelloWorld = pyglet.text.Label("Hello World!",
x = width//2,
y = height - 100,
font_name='Times New Roman',
anchor_x='center', anchor_y='center',
font_size=40

)

# --------Image-------------
image = pyglet.resource.image('ast.jpg')
# image_part = image.get_region(x=300, y=300, width=400, height=400)

# resize image
image.width = image.width//2
image.height = image.height//2

# change image anchor
image.anchor_x = image.width//2
image.anchor_y = image.height//2

# sprite
logo = pyglet.image.load("original.png")
sprite = pyglet.sprite.Sprite(img=logo)
sprite.scale = 0.2
sprite.x, sprite.y = 0, 100
# rotation in degrees
sprite.rotation = 90
t = 200
sound2 = pyglet.media.load("Punch 1.mp3")

def update(dt):
    global t
    if sprite.x > height-100:
        t = -200
        sound2.play()
    elif sprite.x < 0:
        t = 200
        sound2.play()
    sprite.x += dt * t

pyglet.clock.schedule_interval(update, 1/60.)
#  Sprite properties:
#   x/y location, rotation, opacity, color, tint, visibility

# --- audio ----
playing = False
music = pyglet.media.load("Alla-Turca.mp3", streaming=False)
music.volume = 0.2
player = None

@window.event
def on_key_press(symbol, modifier):
    global playing, player
    if symbol == pyglet.window.key.SPACE:
        if playing == False:
            player = music.play()
            playing = True
        else:
            player.pause()
            playing = False

@window.event
def on_draw():
    window.clear()
    image.blit(width//2, height//2)
    sprite.draw()
    HelloWorld.draw()

pyglet.app.run()
