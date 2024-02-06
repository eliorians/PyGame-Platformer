
import pygame

from assets.colors import *

#Player Stats
player_speed = 5
player_jump_height = 5

class Player:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
            self.sprite_sheet = pygame.image.load('./assets/Panda.png')
            self.frame_width = 48
            self.frame_height = 48
            self.num_frames = 8
            self.current_frame = 0
            self.animation_speed = .2
            self.animation_timer = 0
            self.x = 0
            self.y = SCREEN_HEIGHT - self.frame_height

    def draw(self, screen):
        frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
        frame_surface = self.sprite_sheet.subsurface(frame_rect)
        screen.blit(frame_surface, (self.x, self.y))

    def update_animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.animation_timer = 0
    
    def move_left(self):
          if (self.x > 0):
            self.x -= player_speed

    def move_right(self, SCREEN_WIDTH, SCREEN_HEIGHT):
         if(self.x < SCREEN_WIDTH - self.frame_width):
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
        if self.x + self.frame_width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.frame_width
        #bottom edge
        if self.y < 0:
            self.y = 0
        #top edge
        if self.y > SCREEN_HEIGHT - self.frame_height:
            self.y = SCREEN_HEIGHT - self.frame_height