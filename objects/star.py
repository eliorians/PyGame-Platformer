import pygame
from assets.colors import *

class Star:

    def __init__(self, x, y, height, width, image_path):
        # positioning
        self.hitbox = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)  # load the image
        self.image = pygame.transform.scale(self.image, (width, height))  # scale it to the right size

    def draw(self, screen):
        screen.blit(self.image, self.hitbox)  # draw the image
