import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from zombie import Zombie

import world_build_state

name = "ranking_state"

font = None
boy = None

def enter():
    global font
    font = load_font('ENCR10B.TTF', 16)


        boy
