
import pygame

from assets.colors import *

#Player Stats
player_speed = 5
player_jump = 20

class Player:

    def __init__(self, screen_width, screen_height, ground_height):
            #sprite stuff
            self.sprite_sheet = pygame.image.load('./assets/Panda.png')
            self.frame_width = 48
            self.frame_height = 48
            self.num_frames = 8
            self.current_frame = 0
            self.animation_speed = .2
            self.animation_timer = 0
            #position
            self.rect = pygame.Rect(ground_height, screen_height - self.frame_height, self.frame_width, self.frame_height)
            #velocity
            self.velocity_x = 0
            self.velocity_y = 0
            #jumping
            self.is_jumping = False

    def update(self, gravity, dt, screen_width, screen_height):
        self.update_animation(dt)
        self.apply_gravity(gravity)
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
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
        self.velocity_y += gravity

    def stop_moving(self):
        self.velocity_x = 0

    def screenCollisions(self, screen_width, screen_height):
        #left edge
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity_x = 0
        #right edge
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            self.velocity_x = 0 
        #top edge
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity_y = 0
        #bottom edge
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.is_jumping = False
            self.velocity_y = 0

    def lavaCollisions(self, lava):
        if self.rect.colliderect(lava.rect):
            return True
        return False
    
    def starCollisions(self, star):
        if self.rect.colliderect(star.rect):
            return True
        return False
    
    def surfaceCollisions(self, surface):
        if self.rect.colliderect(surface.rect):
            if self.velocity_y > 0:
                    self.rect.bottom = surface.rect.top
                    self.velocity_y = 0
                    self.is_jumping = False
            elif self.velocity_y < 0:
                    self.rect.top = surface.rect.bottom
                    self.velocity_y = 0

    def draw(self, screen):
        frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
        frame_surface = self.sprite_sheet.subsurface(frame_rect)
        screen.blit(frame_surface, self.rect.topleft)

    def update_animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.animation_timer = 0