import game_framework
from pico2d import *

name = "pause_state"
image = None

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del (image)

def update():
    pass

def draw():
    clear_canvas()
    image.clip_draw(250, 250, 400, 400, 800 // 2, 600 // 2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def pause(): pass


def resume(): pass

