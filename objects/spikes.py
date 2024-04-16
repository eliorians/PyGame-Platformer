import pygame
from assets.colors import *

class Spikes:

    def __init__(self, x, y, height, width):
        #positioning
        self.hitbox = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load("assets/spikes.png")  # load the image
        self.image = pygame.transform.scale(self.image, (width, height))  # scale it to the right size

    def draw(self, screen):
        screen.blit(self.image, self.hitbox)
