from assets.colors import *

from surface import Surface
from lava import Lava
from star import Star
import pyautogui

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

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
        Surface(x=0,  width=SCREEN_WIDTH, y=SCREEN_HEIGHT*.90, height=SCREEN_HEIGHT),
        #floating platfrom in center
        Surface(x=SCREEN_WIDTH*.4, width=SCREEN_WIDTH*.2, y=SCREEN_HEIGHT*.7, height=SCREEN_HEIGHT*.05),
    ],
    lava=[
        #lava pit in center
        Lava(x=SCREEN_WIDTH*.4, width=SCREEN_WIDTH*.2, y=SCREEN_HEIGHT*.9, height=SCREEN_HEIGHT),
    ],
    stars=[
        #star on the right side
        Star(x=SCREEN_WIDTH*0.75, width=SCREEN_WIDTH*.05, y=SCREEN_HEIGHT*0.8, height=SCREEN_HEIGHT*.05,),
    ],
)
