import pygame
from assets.colors import *

class Star:

    def __init__(self, x, y, image_path):
        # positioning
        self.hitbox = pygame.Rect(x, y, 40, 30)
        self.image = pygame.image.load(image_path)  # load the image
        self.image = pygame.transform.scale(self.image, (40, 30))

    def draw(self, screen):
        screen.blit(self.image, self.hitbox)  # draw the image
