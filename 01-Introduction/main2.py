import pyglet

class TestWindow(pyglet.window.Window):
    def __init__(self):
        super(TestWindow, self).__init__()
        self.label = pyglet.text.Label('Test Window!')

    def on_draw(self):
        self.clear()
        self.label.draw()

if __name__ == '__main__':
    window = TestWindow()
    pyglet.app.run()
