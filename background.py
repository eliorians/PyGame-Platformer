import pygame
import player
class Background:
    def __init__(self, screen):
        self.screen = screen
        self.bg_images = []
        
        for i in range(1, 6):
            bg_image = pygame.image.load(f"assets/Jungle Asset Pack/parallax background/plx-{i}.png").convert_alpha()
            scaled_image = pygame.transform.scale(bg_image, (screen.get_width(), screen.get_height()))
            self.bg_images.append(scaled_image)
        
        self.bg_width = self.bg_images[0].get_width()

    def draw_bg(self, player):
        for x in range(5):
            speed = 0.3
            for i in self.bg_images:
                self.screen.blit(i, ((x * self.bg_width) - player.scroll * speed, 0))
                speed += 0.1
