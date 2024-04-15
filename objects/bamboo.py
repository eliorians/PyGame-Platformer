import pygame
from assets.colors import *

class Bamboo:

    def __init__(self, x, y):
        # positioning
        self.hitbox = pygame.Rect(x, y, 40, 30)
        self.image = pygame.image.load("assets/bamboo.png")  # load the image
        self.image = pygame.transform.scale(self.image, (80, 60))

        #Blank image
        self.bl_image = pygame.image.load("assets/blank.png")  # load the image
        self.bl_image = pygame.transform.scale(self.bl_image, (80, 60))
        self.here = False

    def draw(self, screen):
        if not self.here:
            screen.blit(self.image, self.hitbox)  
        else:
            screen.blit(self.bl_image, self.hitbox)  