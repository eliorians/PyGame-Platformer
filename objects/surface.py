import pygame
from assets.colors import *

class Surface:

    def __init__(self, x, y, height, width):
        #positioning
        self.hitbox = pygame.Rect(x, y, width, height)
        self.color = green

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.hitbox)