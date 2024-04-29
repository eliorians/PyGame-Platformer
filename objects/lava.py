import pygame
from assets.colors import *

class Lava:

    def __init__(self, x, y, height, width):
        #positioning
        self.hitbox = pygame.Rect(x, y, width, height)
        self.color = red

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.hitbox)
