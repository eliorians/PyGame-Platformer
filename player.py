
import pygame
import time

from assets.colors import *

#Player Stats
player_speed = 5
player_jump = 10

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
            #position
            self.x = 0
            self.y = screen_height - self.frame_height
            #velocity
            self.velocity_x = 0
            self.velocity_y = 0
            #jumping
            self.jump_cooldown = 500  # 500 milliseconds
            self.last_jump_time = 0
            self.is_jumping = False

    def update(self, gravity, dt, screen_width, screen_height):
        self.update_animation(dt)
        self.apply_gravity(gravity)
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.screenCollisions(screen_width, screen_height)
    
    def move_left(self):
        self.velocity_x = -player_speed

    def move_right(self):
        self.velocity_x = player_speed

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -player_jump

    def apply_gravity(self, gravity):
        # apply gravity if not jumping
        if not self.is_jumping:
            self.velocity_y += gravity

    def stop_moving(self):
        self.velocity_x = 0

    def screenCollisions(self, screen_width, screen_height):
        #left edge
        if self.x < 0:
            self.x = 0
            self.velocity_x = 0
        #right edge
        if self.x + self.frame_width > screen_width:
            self.x = screen_width - self.frame_width
            self.velocity_x = 0 
        #top edge
        if self.y < 0:
            self.y = 0
            self.velocity_y = 0

        #bottom edge
        if self.y > screen_height - self.frame_height:
            self.y = screen_height - self.frame_height
            self.is_jumping = False
            self.velocity_y = 0

    def lavaCollisions(self, lava):
        player_rect = pygame.Rect(self.x, self.y, self.frame_width, self.frame_height)
        if player_rect.colliderect(lava.rect):
            return True
        return False
    
    #todo fix this
    def surfaceCollisions(self, surface):
        player_rect = pygame.Rect(self.x, self.y, self.frame_width, self.frame_height)
        if player_rect.colliderect(surface.rect):
            return True
        return False

    def draw(self, screen):
        frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
        frame_surface = self.sprite_sheet.subsurface(frame_rect)
        screen.blit(frame_surface, (self.x, self.y))

    def update_animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.animation_timer = 0