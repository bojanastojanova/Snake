# how to stop the snake from going to (-1,0) or to (10,0)?
# Is it ok if I define snake and fruit as global variables? If not, how to work with them as local variables?

from random import randrange
from pyglet.window import key
import pyglet
from pathlib import Path

TILES_DIRECTORY = Path('snake-tiles')

snake_tiles = {}
for path in TILES_DIRECTORY.glob('*.png'):
    snake_tiles[path.stem] = pyglet.image.load(path)

print(snake_tiles)

PXL_SIZE=64
WINDOW_WID = 10
WINDOW_HEI = 10

# create the snake. The starting coordinates of the snake are always the same
# and are given as default attribute in the __init__ attribute
# I also define the head  as separate attribute which can be useful when
# defining the movement of the Snake
# the starting direction of the snake is also given by default (up)
# the snake has methods move and eat which respectively make it move or increase
# length by one unit.
class Snake:
    def __init__(self, coordinates = [(0,0),(0,1),(0,2)],dir=(0,1)):   # the starting snake coordinates are always the same
        self.position = coordinates
        self.head = coordinates[-1]
        self.dir = dir
        self.alive = True
    def move(self):
        new_head=(self.head[0] + self.dir[0], self.head[1] + self.dir[1])
        self.position.append(new_head)
        self.head = new_head
        del self.position[0]
    def eat(self):   # for now the module exists, but I'm not using it
        new_head=(self.head[0] + self.dir[0], self.head[1] + self.dir[1])
        self.position.append(new_head)
        self.head = new_head

snake=Snake()

class Fruit:
    def __init__(self, coordinates):
        self.position = coordinates
        self.eaten = False
    def new(self):
        self.position = (randrange((WINDOW_WID-1)),randrange((WINDOW_HEI-1)))
        while self.position in snake.position:
            self.position = (randrange(WINDOW_WID-1),randrange(WINDOW_HEI-1))
            print(self.position)

fruit = Fruit((randrange(WINDOW_WID-1),randrange(WINDOW_HEI-1))) # how do I generate the first fruit on a random position?
# I can't seem to make new fruit after the first one is eaten

        # fuit.eaten = True when there is no fruit in the playing field (i.e. at
        # the begining of the game or when snake.head == fruit.position). If
        # fruit.eaten == True then a new fruit with a new pair of coordinates
        # is made.


img = pyglet.image.load('apple.png')
apple = pyglet.sprite.Sprite(img)

# drawing functions
def draw_snake(snake):
    for coordinate in snake.position:
        green.x=coordinate[0]*PXL_SIZE
        green.y=coordinate[1]*PXL_SIZE
        green.draw()

def draw_fruit(fruit):
    apple.x = fruit.position[0]*PXL_SIZE
    apple.y = fruit.position[1]*PXL_SIZE
    apple.draw()

def snake_lives():
    if snake.head[0] >= 0 and snake.head[0] < WINDOW_WID-1 and snake.head[1] >= 0 and snake.head[1] < WINDOW_HEI - 1 and snake.head not in snake.position[:-1] :
        snake.alive=True
        return snake
    else:
        snake.alive=False
        return snake

# Functions to be recorded
def draw():
    window.clear()
    draw_fruit(fruit)
    draw_snake(snake)

def tick(t):
    snake_lives()
    if snake.alive == True:
        if snake.head == fruit.position:
            snake.eat()
            fruit.new()
        else:
            snake.move()

def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        snake.dir = (0,1)
    if symbol == key.DOWN:
        snake.dir = (0,-1)
    if symbol == key.RIGHT:
        snake.dir = (1,0)
    if symbol == key.LEFT:
        snake.dir = (-1,0)

window = pyglet.window.Window(width=WINDOW_WID*PXL_SIZE, height=WINDOW_HEI*PXL_SIZE)

img = pyglet.image.load('green.png')
green = pyglet.sprite.Sprite(img)

#while snake.alive == True, schedule_interval
pyglet.clock.schedule_interval(tick, 1/2)
# if snake.alive == False, clock.unschedule

window.push_handlers(on_draw=draw,
                     on_key_press=on_key_press,
)

pyglet.app.run()
