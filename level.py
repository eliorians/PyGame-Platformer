import pygame
from assets import *

from objects.surface import Surface
from objects.lava import Lava
from objects.enemy import Enemy
from objects.star import Star
from objects.bamboo import Bamboo
from objects.spikes import Spikes 
from objects.moon import Moon
from objects.info import Info
from main import SCREEN_WIDTH, SCREEN_HEIGHT

class Level:

    def __init__(self, surfaces, lava, stars, enemys, bamboo, spikes, moons, info):
        self.surfaces = surfaces
        self.lava = lava
        self.stars = stars
        self.enemy = enemys
        self.bamboo = bamboo        
        self.spikes = spikes
        self.moon = moons
        self.info = info

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
        for spikes in self.spikes:
            spikes.draw(screen)
        for moon in self.moon:
            moon.draw(screen)
        for info in self.info:
            info.draw(screen)

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
    ],
    spikes=[
    ],
    moons=[
    ],
    info=[
        Info(info="Grab the dumpling to win the level!", x=600, y=300, width=100, height=100)
    ]
)

#Level Two
level2 = Level(
    surfaces=[
        # floating platform on the left
        Surface(x= 0, width=SCREEN_WIDTH * 0.45, y=SCREEN_HEIGHT * 0.5, height=SCREEN_HEIGHT * 0.05),
        # floating platform on the right
        Surface(x= 490, width=SCREEN_WIDTH , y=SCREEN_HEIGHT * 0.5, height=SCREEN_HEIGHT * 0.05),
    ],
    lava=[
        # lava across the bottom
        Lava(x=0, width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.83, height=SCREEN_HEIGHT),
    ],
    stars=[
        # star at the end of the right floating platform
        Star(x=SCREEN_WIDTH * 0.9 - SCREEN_WIDTH * 0.05, y=SCREEN_HEIGHT*0.45),
    ],
    enemys=[
        Enemy(start_x=415, end_x=415, start_y=100, end_y=450, velocity=2, horizontal=False)
    ],
    moons=[
    ],
    spikes=[
    ],
    bamboo=[
    ],
    info=[
        Info(info="Avoid the jigglypuff, it will hurt you!", x=200, y=100, width=150, height=75)
    ]
)

#Level Three - Carson's Level
level3 = Level(
    surfaces=[
        Surface(x=0, width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.83, height=SCREEN_HEIGHT),
        Surface(x= 450, width=SCREEN_WIDTH , y=SCREEN_HEIGHT * 0.2, height=SCREEN_HEIGHT * 0.05),
    ],
    lava=[
    ],
    stars=[
        Star(x=SCREEN_WIDTH * 0.8, y=SCREEN_HEIGHT*0.1),
    ],
    enemys=[
        Enemy(start_x=100, end_x=400, start_y=SCREEN_HEIGHT*.78, end_y=500, velocity=2, horizontal=True)
    ],
    bamboo=[
        Bamboo(x=SCREEN_WIDTH * 0.8, y=SCREEN_HEIGHT*0.7),
    ],
    moons=[
    ],
    spikes=[
    ],
    info=[
        Info(info="Grab the bamboo to boost your jump!", x=500, y=300, width=150, height=75)
    ]
)

#Level 4 - Aaron's Level
level4 = Level(
    surfaces=[
        Surface(x= 0, width=SCREEN_WIDTH * 0.4, y=SCREEN_HEIGHT * 0.7, height=SCREEN_HEIGHT * 0.05),
        Surface(x= 450, width=SCREEN_WIDTH , y=SCREEN_HEIGHT * 0.5, height=SCREEN_HEIGHT * 0.05),
        Surface(x= 250, width=SCREEN_WIDTH * 0.3, y=SCREEN_HEIGHT * 0.3, height=SCREEN_HEIGHT * 0.05)
    ],
    lava=[
        Lava(x=0,  width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.83, height=SCREEN_HEIGHT),
    ],
    stars=[
        
        Star(x=SCREEN_WIDTH * 0.8, y=SCREEN_HEIGHT*0.4),
    ],
    enemys=[
        Enemy(start_x=SCREEN_WIDTH / 2, end_x=SCREEN_WIDTH / 2, start_y=220, end_y=375, velocity=2, horizontal=False)
    ],
    bamboo=[
        Bamboo(x=SCREEN_WIDTH * 0.2, y=SCREEN_HEIGHT*0.6),
    ],
    spikes=[
        Spikes(x=SCREEN_WIDTH * 0.38 - SCREEN_WIDTH * 0.05, width=SCREEN_WIDTH*0.11, y=SCREEN_HEIGHT*0.32, height=SCREEN_HEIGHT*0.05),
        Spikes(x=SCREEN_WIDTH * 0.52 - SCREEN_WIDTH * 0.05, width=SCREEN_WIDTH*0.11, y=SCREEN_HEIGHT*-0.03, height=SCREEN_HEIGHT*0.05),
    ],
    moons=[
    ],
    info=[
        Info(info="Avoid the spikes, they will hurt you!", x=50, y=100, width=100, height=125)
    ]
)
level5 = Level(
   surfaces=[
        Surface(x=0, width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.95, height=SCREEN_HEIGHT),
        # Surface(x=350, width=100, y=600, height=500),
        Surface(x=SCREEN_WIDTH // 2 - 25, width=50, y=100, height=SCREEN_HEIGHT),  # Vertical surface from bottom to middle, slightly taller
    ],
    lava=[
    ],
    stars=[
        Star(x=SCREEN_WIDTH * 0.9 - SCREEN_WIDTH * 0.05, y=SCREEN_HEIGHT * 0.45),
    ],
    enemys=[
    ],
    bamboo=[
    ],
    spikes=[
    ],
    moons=[
        Moon(x=200, y=500),
        Moon(x=650, y =0),
    ],
    info=[
        Info(info="Pick up the potion to flip gravity!", x=50, y=100, width=75, height=100)
    ]
)
