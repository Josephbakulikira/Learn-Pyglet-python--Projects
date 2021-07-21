import pyglet

mine = pyglet.image.load('./assets/mine.png')
flag = pyglet.image.load('./assets/flag.png')


class Cell(pyglet.shapes.Rectangle):
    def __init__(self, x, y, width, height):
        super(Cell, self).__init__(x, y, width, height)

        self.isActive = False
        self.isFlagged = False
        self.isMine = False

        self.cell_size = 50
        self.secondaryColor = (100, 100, 100)
        self.count = 0 # neighbor count

        # sprites
        self.flagSprite = pyglet.sprite.Sprite(img=flag)
        self.mineSprite = pyglet.sprite.Sprite(img=mine)
        self.flagSprite.scale = 1/(width/2)
        self.flagSprite.x = self.x + width/3
        self.flagSprite.y = self.y + width/3
        self.mineSprite.scale = 1/(width/3)
        self.mineSprite.x = self.x + self.mineSprite.width/3
        self.mineSprite.y = self.y + self.mineSprite.width/3



    def update(self, m):
        if self.isActive == True:
            self.color = self.secondaryColor

    def floodFill(x, y ,grid):
        if Cell.isFillable(x, y, grid):
            grid[x][y].isActive = True
            if grid[x][y].count == 0 :
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        _x = x + i
                        _y = y + j
                        if _x != x or _y != y:
                            Cell.floodFill(_x, _y, grid)

        return

    def isFillable(x, y, grid):
        if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]):
            if grid[x][y].isActive != True and grid[x][y].isMine == False:
                print("here2")
                return True
            else:
                return False

        return False
    def activate(self, x, y, grid, Event="LEFT"):
        if Event == "RIGHT":
            self.isFlagged = not self.isFlagged
        else:
            if self.count == 0:
                print("here1")
                Cell.floodFill(x, y, grid)
            self.isActive = True



    def countMines(self, grid):
        counter = 0
        if self.isMine == True:
            self.count = -1
            return
        for x in range(-1, 2):
            for y in range(-1, 2):
                if self.x//self.cell_size + x < len(grid) and self.y//self.cell_size + y < len(grid[0]):
                    neighbor = grid[self.x//self.cell_size + x ][ self.y//self.cell_size + y]
                    if neighbor.isMine == True:
                        counter += 1
        self.count =  counter
        color = (0, 0, 255, 255)
        if self.count <= 1:
            color = (0, 0, 255, 255)
        elif self.count == 2:
            color = (0, 255, 0, 255)
        elif self.count == 3:
            color = (255, 0, 0, 255)
        else:
            color = (255, 50, 255, 255)

        if self.isMine == False:
            self.text = pyglet.text.Label(
            str(self.count),
            x= self.x + self.cell_size//2,
            y = self.y + self.cell_size//2,
            anchor_x='center',
            anchor_y='center',
            font_size=30,
            font_name="Verdana",
            bold=True)
            self.text.color = color



    def show(self):
        self.draw()
        if self.isActive == True:
            if self.isMine == True:
                self.mineSprite.draw()
            elif self.count > 0:
                self.text.draw()
        elif self.isFlagged == True:
            self.flagSprite.draw()
