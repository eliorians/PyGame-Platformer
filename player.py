
import pygame

from assets.colors import *

#Player Stats
player_speed = 5
player_jump = 20

class Player:

    def __init__(self, screen_width, screen_height, x, y):
            #sprite stuff
            self.sprite_sheet = pygame.image.load('./assets/Panda.png')
            self.frame_width = 48
            self.frame_height = 48
            self.num_frames = 8
            self.current_frame = 0
            self.animation_speed = .2
            self.animation_timer = 0
            #starting position and hitbox
            self.hitbox = pygame.Rect(x, y, 32, 32)
            #velocity
            self.velocity_x = 0
            self.velocity_y = 0
            #jumping
            self.is_jumping = False
            #background scroll
            self.scroll = 0

    def update(self, gravity, dt, screen_width, screen_height):
        self.update_animation(dt)
        self.apply_gravity(gravity)
        self.hitbox.x += self.velocity_x
        self.hitbox.y += self.velocity_y
        self.screenCollisions(screen_width, screen_height)
        self.update_scroll()
    
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
        if self.hitbox.left < 0:
            self.hitbox.left = 0
            self.velocity_x = 0
        #right edge
        if self.hitbox.right > screen_width:
            self.hitbox.right = screen_width
            self.velocity_x = 0 
        #top edge
        if self.hitbox.top < 0:
            self.hitbox.top = 0
            self.velocity_y = 0
        #bottom edge
        if self.hitbox.bottom > screen_height:
            self.hitbox.bottom = screen_height
            self.is_jumping = False
            self.velocity_y = 0

    def lavaCollisions(self, lava):
        if self.hitbox.colliderect(lava.hitbox):
            return True
        return False
    
    def starCollisions(self, star):
        if self.hitbox.colliderect(star.hitbox):
            return True
        return False
    
    def surfaceCollisions(self, surface):
        if self.hitbox.colliderect(surface.hitbox):
            #jumping on top of the surface
            if self.velocity_y > 0:
                    self.hitbox.bottom = surface.hitbox.top
                    self.velocity_y = 0
                    self.is_jumping = False
            #jumping into the bottom of the surface
            elif self.velocity_y < 0:
                    self.hitbox.top = surface.hitbox.bottom
                    self.velocity_y = 0

    def draw(self, screen):
        #get offset to recenter the players hitbox
        offset_x = (self.hitbox.width - self.frame_width) // 2
        offset_y = (self.hitbox.height - self.frame_height) // 2
        frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
        frame_surface = self.sprite_sheet.subsurface(frame_rect)
        screen.blit(frame_surface, (self.hitbox.left + offset_x, self.hitbox.top + offset_y))

        #white outline of the player's hitbox
        pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 1)


    def update_animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.animation_timer = 0

    def update_scroll(self):
        if self.velocity_x < 0 and self.scroll > 0:
            self.scroll -= 5
        elif self.velocity_x > 0 and self.scroll < 3000:
            self.scroll += 5
