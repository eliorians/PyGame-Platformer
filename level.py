import pygame
from assets.colors import *

from objects.surface import Surface
from objects.lava import Lava
from objects.enemy import Enemy
from objects.star import Star

from main import SCREEN_WIDTH, SCREEN_HEIGHT

class Level:

    def __init__(self, surfaces, lava, stars, enemys):
        self.surfaces = surfaces
        self.lava = lava
        self.stars = stars
        self.enemy = enemys


    def draw(self, screen):
        for surface in self.surfaces:
            surface.draw(screen)
        for lava in self.lava:
            lava.draw(screen)
        for star in self.stars:
            star.draw(screen)
        for enemy in self.enemy:
            enemy.draw(screen)

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
        #floating platform in center
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
    enemys=[
    ]
)
#Level Two
level2 = Level(
    surfaces=[
        # ground surface
        Surface(x=0, width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.95, height=SCREEN_HEIGHT),
        # floating platform on the left
        Surface(x= 0, width=SCREEN_WIDTH * 0.4, y=SCREEN_HEIGHT * 0.5, height=SCREEN_HEIGHT * 0.05),

        # floating platform on the right
        Surface(x= 450, width=SCREEN_WIDTH , y=SCREEN_HEIGHT * 0.5, height=SCREEN_HEIGHT * 0.05),
    ],
    lava=[
        # lava pit at the beginning
        Lava(x=0,  width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.83, height=SCREEN_HEIGHT),
    ],
    stars=[
        # star at the end of the right floating platform
        Star(x=SCREEN_WIDTH*0.9, width=SCREEN_WIDTH*.05, y=SCREEN_HEIGHT*0.45, height=SCREEN_HEIGHT*.03,),       
    ],
    enemys=[
        Enemy(start_x=400, end_x=400, start_y=0, end_y=600, velocity=3, horizontal=False)
    ]
)
