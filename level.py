
import pygame
from assets.colors import *

from surface import Surface
from lava import Lava
from star import Star
import ctypes

user32 = ctypes.windll.user32
SCREEN_WIDTH=user32.GetSystemMetrics(0)
SCREEN_HEIGHT=user32.GetSystemMetrics(1)

class Level:

    def __init__(self, surfaces, lava, stars):
        self.surfaces = surfaces
        self.lava = lava
        self.stars = stars

    def draw(self, screen):
        for surface in self.surfaces:
            surface.draw(screen)
        for lava in self.lava:
            lava.draw(screen)
        for star in self.stars:
            star.draw(screen)

class Levels:
    def __init__(self):
        self.level_list = []
        self.current_level_index = 0

    def add_level(self, level):
        self.level_list.append(level)

    @property
    def current_level(self):
        return self.level_list[self.current_level_index]
    
    @current_level.setter
    def current_level(self, index):
        self.current_level_index = index

#Level One

level1 = Level(
    surfaces=[
        #ground surface
        Surface(x=0, y=SCREEN_HEIGHT*.90, height=SCREEN_HEIGHT, width=SCREEN_WIDTH),
        #floating platfrom
        Surface(x=SCREEN_WIDTH*.4, y=SCREEN_HEIGHT*.7, height=SCREEN_HEIGHT*.3, width=SCREEN_WIDTH*.2),
    ],
    lava=[
        Lava(x=300, y=SCREEN_HEIGHT-30, height=30, width=250),
    ],
    stars=[
        Star(x=750, y=550, height=10, width=10),
    ],
)
