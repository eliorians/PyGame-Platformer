
import pygame
from assets.colors import *

class Enemy:
    def __init__(self, start_x, start_y, end_x, end_y, velocity, horizontal):
        self.hitbox = pygame.Rect(start_x, start_y, 32, 32)
        self.patrol_point1 = (start_x, start_y)
        self.patrol_point2 = (end_x, end_y)
        self.velocity = velocity
        self.horizontal = horizontal
        self.image = pygame.image.load("assets/jiggly.png")
        self.image = pygame.transform.scale(self.image, (40, 30))

    def update(self):
        if self.horizontal:
            # Update horizontal position
            self.hitbox.x += self.velocity

            # Change direction if we hit a patrol point
            if self.velocity > 0 and self.hitbox.x >= self.patrol_point2[0]:
                self.velocity *= -1
            elif self.velocity < 0 and self.hitbox.x <= self.patrol_point1[0]:
                self.velocity *= -1
        else:
            # Update vertical position
            self.hitbox.y += self.velocity

            # Change direction if we hit a patrol point
            if self.velocity > 0 and self.hitbox.y >= self.patrol_point2[1]:
                self.velocity *= -1
            elif self.velocity < 0 and self.hitbox.y <= self.patrol_point1[1]:
                self.velocity *= -1

    def draw(self, screen):
        screen.blit(self.image, self.hitbox)

