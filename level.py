
import pygame
from assets.colors import *

from surface import Surface
from lava import Lava
from star import Star

SCREEN_WIDTH=1920
SCREEN_HEIGHT=1080

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

level1 = Level(
    surfaces=[
        Surface(x=0, y=SCREEN_HEIGHT-30, height=30, width=SCREEN_WIDTH),    #ground
        Surface(x=250, y=500, height=30, width=250),                        #floating platform
    ],
    lava=[
        Lava(x=300, y=SCREEN_HEIGHT-30, height=30, width=250),
    ],
    stars=[
        Star(x=750, y=550, height=10, width=10),
    ],
)
