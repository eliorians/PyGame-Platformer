import pygame
from assets import *

from objects.surface import Surface
from objects.lava import Lava
from objects.enemy import Enemy
from objects.star import Star
from objects.bamboo import Bamboo

from main import SCREEN_WIDTH, SCREEN_HEIGHT


class Level:

    def __init__(self, surfaces, lava, stars, enemys, bamboo):
        self.surfaces = surfaces
        self.lava = lava
        self.stars = stars
        self.enemy = enemys
        self.bamboo = bamboo


    def draw(self, screen):
        for surface in self.surfaces:
            surface.draw(screen)
        for lava in self.lava:
            lava.draw(screen)
        for star in self.stars:
            star.draw(screen)
        for enemy in self.enemy:
            enemy.draw(screen)
        for bamboo in self.bamboo:
            bamboo.draw(screen)

class Levels:
    def __init__(self):
        self.level_list = []
        self.current_level_index = 1

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
        return self.level_list[self._current_level_index - 1]

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
        Star(x=SCREEN_WIDTH*0.9, y=SCREEN_HEIGHT*0.85),
    ],
    enemys=[
    ],
    bamboo=[

    ]
)
#Level Two
level2 = Level(
    surfaces=[
        # floating platform on the left
        Surface(x= 0, width=SCREEN_WIDTH * 0.45, y=SCREEN_HEIGHT * 0.5, height=SCREEN_HEIGHT * 0.05),
        # floating platform on the right
        Surface(x= 470, width=SCREEN_WIDTH , y=SCREEN_HEIGHT * 0.5, height=SCREEN_HEIGHT * 0.05),
    ],
    lava=[
        # lava across the bottom
        Lava(x=0, width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.83, height=SCREEN_HEIGHT),
    ],
    stars=[
        # star at the end of the right floating platform
        Star(x=SCREEN_WIDTH * 0.8, y=SCREEN_HEIGHT*0.4),
    ],
    enemys=[
<<<<<<< HEAD
        Enemy(start_x=425, end_x=425, start_y=100, end_y=500, velocity=2, horizontal=False)
    ],
    bamboo=[

    ]
)

#Level Three - Carson's Level
level3 = Level(
    surfaces=[
        # floating platform on the left
        Surface(x=0, width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.83, height=SCREEN_HEIGHT),
        # floating platform on the right
        Surface(x= 450, width=SCREEN_WIDTH , y=SCREEN_HEIGHT * 0.2, height=SCREEN_HEIGHT * 0.05),
    ],
    lava=[
        
    ],
    stars=[
        # star at the end of the right floating platform
        Star(x=SCREEN_WIDTH * 0.8, y=SCREEN_HEIGHT*0.1, image_path="assets/dumplin.png"),
    ],
    enemys=[
        Enemy(start_x=100, end_x=400, start_y=SCREEN_HEIGHT*.78, end_y=500, velocity=2, horizontal=True)
    ],
    bamboo=[
        # Makes you jump high
        Bamboo(x=SCREEN_WIDTH * 0.8, y=SCREEN_HEIGHT*0.7, image_path="assets/bamboo.png"),
=======
        # enemy patroling vertically in center
        Enemy(start_x=SCREEN_WIDTH / 2, end_x=SCREEN_WIDTH / 2, start_y=150, end_y=375, velocity=2, horizontal=False)
>>>>>>> e7b3a48c5dd220c32ea4483911cd08df280c0430
    ]
)
