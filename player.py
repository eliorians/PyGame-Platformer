
import pygame
import sys

from assets.colors import *

#Player Stats
player_speed = 5

class Player:

    def __init__(self, screen_width, screen_height):
            #sprite stuff
            self.sprite_sheet = pygame.image.load('./assets/Panda.png')
            self.frame_width = 48
            self.frame_height = 48
            self.num_frames = 8
            self.current_frame = 0
            self.animation_speed = .2
            self.animation_timer = 0
            #starting position
            self.x = 0
            self.y = screen_height - self.frame_height
            #Jumping Mecs
            self.player_jump_height = 15
            self.jump_cooldow = 3
            self.last_jump_time = 0

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

    def move_right(self, screen_width, screen_height):
         if(self.x < screen_width - self.frame_width):
              self.x += player_speed

    #TODO: make player only able to jump x times
    def jump(self, current_time):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_jump_time >= self.jump_cooldow:
            self.y -= self.player_jump_height
            self.last_jump_time = current_time

    def apply_gravity(self, gravity):
         self.y += gravity

    def screenCollisions(self, screen_width, screen_height):
        #left edge
        if self.x < 0:
            self.x = 0
        #right edge
        if self.x + self.frame_width > screen_width:
            self.x = screen_width - self.frame_width
        #bottom edge
        if self.y < 0:
            self.y = 0
        #top edge
        if self.y > screen_height - self.frame_height:
            self.y = screen_height - self.frame_height

    def lavaCollisions(self, lava):
        player_rect = pygame.Rect(self.x, self.y, self.frame_width, self.frame_height)
        if player_rect.colliderect(lava.rect):
            return True
        return False
    
    def surfaceCollisions(self, surface):
        player_rect = pygame.Rect(self.x, self.y, self.frame_width, self.frame_height)
        if player_rect.colliderect(surface.rect):
            #player collides with top
            if player_rect.bottom > surface.rect.top:
                self.y = surface.rect.top - self.frame_height
            #player collides with bottom
            elif player_rect.top < surface.rect.bottom:
                self.y = surface.rect.bottom
            #player collides to the right
            if player_rect.right > surface.rect.left:
                self.x = surface.rect.left - self.frame_width
            #player collides with left
            elif player_rect.left < surface.rect.right:
                self.x = surface.rect.right

