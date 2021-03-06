from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def MakeRectangle() :
    def MoveFromCenerToRight():
        x, y = 800 // 2, 90
        while x < 800 - 25:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.01)

    def MoveUp():
        x, y = 800 - 25, 90
        while y < 600 - 50:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y += 2
            delay(0.01)

    def MoveLeft():
        x, y = 800 - 25, 600 - 50
        while x > 0 + 25:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x -= 2
            delay(0.01)

    def MoveDown():
        x, y = 0 + 25, 600 - 50
        while y > 0 + 90:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y -= 2
            delay(0.01)

    def MoveFromLeftToCenter():
        x, y = 0 + 25, 90
        while x < 800 // 2:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.01)

    MoveFromCenerToRight()
    MoveUp()
    MoveLeft()
    MoveDown()
    MoveFromLeftToCenter()

import math

def MakeCircle() :
    cx, cy, r = 800 // 2, 600 // 2, (600 - 180) // 2
    degree = -90
    while degree < 270 :
        radian = math.radians(degree)
        x = cx + r * math.cos(radian)
        y = cy + r * math.sin(radian)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        degree += 1
        delay(0.01)

while True :
    MakeRectangle()
    MakeCircle()

    
close_canvas()    
