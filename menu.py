from main import SCREEN_WIDTH, SCREEN_HEIGHT

import pygame
import sys

class menu:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options

    def draw_menu(self):
        image_path = "C:\Users\Eli Orians\Desktop\Repo\PyGame-Platformer\\assets\CARSON.png"
