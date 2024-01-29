
import pygame

from assets.colors import *

#Player Stats
player_width = 100
player_height = 100
player_speed = 5
player_jump_height = 5

class Player:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, GRAVITY):
            self.x = SCREEN_WIDTH // 2 - player_width // 2
            self.y = SCREEN_HEIGHT - player_height - 10
    
    def draw(self, screen):
        pygame.draw.rect(screen, blue, (self.x, self.y, player_width, player_height))
    
    def move_left(self):
          if (self.x > 0):
            self.x -= player_speed

    def move_right(self, SCREEN_WIDTH, SCREEN_HEIGHT):
         if(self.x < SCREEN_WIDTH - player_width):
              self.x += player_speed

    #TODO: make player only able to jump x times
    def jump(self):
        self.y -= player_jump_height

    def apply_gravity(self, GRAVITY):
         self.y += GRAVITY

    def handle_collisions(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        #left edge
        if self.x < 0:
            self.x = 0
        #right edge
        elif self.x > SCREEN_WIDTH - player_width:
            self.x = SCREEN_WIDTH - player_width
        #bottom edge
        if self.y < 0:
            self.y = 0
        #top edge
        elif self.y > SCREEN_HEIGHT - player_height:
            self.y = SCREEN_HEIGHT - player_height