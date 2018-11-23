import random
from pico2d import *
import game_world
import game_framework
from boy import Boy


class Ball:
    image = None

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1600-1), random.randint(0, 1600-1)
        self.dx = self.x - self.Boy.cx
        self.dy = self.y - self.Boy.cy

    def get_bb(self):
        return self.dx - 10, self.dy - 10, self.dx + 10, self.dy + 10

    def draw(self):
        self.image.draw(self.dx, self.dx)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.dx = self.x - self.Boy.cx
        self.dy  = self.y - self.Boy.cy


