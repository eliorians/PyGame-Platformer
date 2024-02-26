import pygame
from assets.colors import *

class Star:

    def __init__(self, x, y, height, width):
        #positioning
        self.rect = pygame.Rect(x, y, width, height)
        self.color = yellow

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
