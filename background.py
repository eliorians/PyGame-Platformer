import pygame
import sys

class ParallaxBackground:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Set up background images
        self.bg_layer1 = pygame.image.load('./assets/Jungle Asset Pack/parallax background/plx-1.png')
        self.bg_layer2 = pygame.image.load('./assets/Jungle Asset Pack/parallax background/plx-2.png')
        self.bg_layer3 = pygame.image.load('./assets/Jungle Asset Pack/parallax background/plx-3.png')
        self.bg_layer4 = pygame.image.load('./assets/Jungle Asset Pack/parallax background/plx-4.png')
        self.bg_layer5 = pygame.image.load('./assets/Jungle Asset Pack/parallax background/plx-5.png')

        # Resize background images to match the screen size
        self.bg_layer1 = pygame.transform.scale(self.bg_layer1, (screen_width, screen_height))
        self.bg_layer2 = pygame.transform.scale(self.bg_layer2, (screen_width, screen_height))
        self.bg_layer3 = pygame.transform.scale(self.bg_layer3, (screen_width, screen_height))
        self.bg_layer4 = pygame.transform.scale(self.bg_layer4, (screen_width, screen_height))
        self.bg_layer5 = pygame.transform.scale(self.bg_layer5, (screen_width, screen_height))

        # Set initial fractional positions for the layers
        self.layer1_x = 0.0
        self.layer2_x = 0.0
        self.layer3_x = 0.0
        self.layer4_x = 0.0
        self.layer5_x = 0.0

        # Set speeds for the layers
        self.layer1_speed = 1
        self.layer2_speed = 1
        self.layer3_speed = 1
        self.layer4_speed = 1
        self.layer5_speed = 1

    def update(self, player_is_moving):
        if player_is_moving:
            # Update fractional layer positions based on speeds
            self.layer1_x -= self.layer1_speed
            self.layer2_x -= self.layer2_speed
            self.layer3_x -= self.layer3_speed
            self.layer4_x -= self.layer4_speed
            self.layer5_x -= self.layer5_speed

            # Wrap around the background layers when they go off-screen
            self.layer1_x %= 1.0
            self.layer2_x %= 1.0
            self.layer3_x %= 1.0
            self.layer4_x %= 1.0
            self.layer5_x %= 1.0

    def draw(self, screen):
        # Draw background layers using fractional positions for smooth movement
        screen.blit(self.bg_layer1, (self.layer1_x * self.screen_width, 0))
        screen.blit(self.bg_layer2, (self.layer2_x * self.screen_width, 0))
        screen.blit(self.bg_layer3, (self.layer3_x * self.screen_width, 0))
        screen.blit(self.bg_layer4, (self.layer4_x * self.screen_width, 0))
        screen.blit(self.bg_layer5, (self.layer5_x * self.screen_width, 0))