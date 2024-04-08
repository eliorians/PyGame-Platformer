import pygame
from assets.colors import *

from objects.surface import Surface
from objects.lava import Lava
from objects.star import Star

from main import SCREEN_WIDTH, SCREEN_HEIGHT

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
    def current_level_index(self):
        return self._current_level_index
    
    @current_level_index.setter
    def current_level_index(self, index):
        self._current_level_index = index

    @property
    def current_level(self):
        return self.level_list[self._current_level_index]

#Level One
level1 = Level(
    surfaces=[
        #ground surface
        Surface(x=0,  width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.95, height=SCREEN_HEIGHT),
        #floating platfrom in center
        #the formula in X ensures its centered, so long as the width is using the same value
        Surface(x=(SCREEN_WIDTH - (SCREEN_WIDTH * 0.3)) / 2, width=SCREEN_WIDTH*.3, y=SCREEN_HEIGHT*.8, height=SCREEN_HEIGHT*.05),
    ],
    lava=[
        #lava pit in center
        Lava(x=(SCREEN_WIDTH - (SCREEN_WIDTH * 0.4)) / 2, width=SCREEN_WIDTH*.4, y=SCREEN_HEIGHT*.95, height=SCREEN_HEIGHT),
    ],
    stars=[
        #star on the right side
        Star(x=SCREEN_WIDTH*0.9, width=SCREEN_WIDTH*.05, y=SCREEN_HEIGHT*0.85, height=SCREEN_HEIGHT*.05,),
    ],
)
#Level Two
level2 = Level(
    surfaces=[
        # ground surface
        Surface(x=0, width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.95, height=SCREEN_HEIGHT),
        # floating platform on the left
        Surface(x= 5 , width=SCREEN_WIDTH * 0.4, y=SCREEN_HEIGHT * 0.7, height=SCREEN_HEIGHT * 0.05),

        # floating platform on the right
        Surface(x=SCREEN_WIDTH * 0.6, width=SCREEN_WIDTH * 0.3, y=SCREEN_HEIGHT * 0.6, height=SCREEN_HEIGHT * 0.05),
    ],
    lava=[
        # lava pit at the beginning
        Lava(x=0, width=SCREEN_WIDTH * 0.2, y=SCREEN_HEIGHT * 0.95, height=SCREEN_HEIGHT),
        # lava pit on the left
        Lava(x=0, width=SCREEN_WIDTH * 1, y=SCREEN_HEIGHT * 0.95, height=SCREEN_HEIGHT),
        # lava pit on the right
        Lava(x=SCREEN_WIDTH * 0.9, width=SCREEN_WIDTH * 0.1, y=SCREEN_HEIGHT * 0.95, height=SCREEN_HEIGHT),
    ],
    stars=[
        # star at the end of the right floating platform
        Star(x=SCREEN_WIDTH * 0.9 - SCREEN_WIDTH * 0.05, width=SCREEN_WIDTH*0.05, y=SCREEN_HEIGHT*0.6, height=SCREEN_HEIGHT*0.05),
]
)
