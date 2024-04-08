import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.menu_background = pygame.image.load("assets/PandaMainMenu.png").convert_alpha()
        self.menu_background = pygame.transform.scale(self.menu_background, (800, 600))

    def draw(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Blit the menu background onto the screen
        self.screen.blit(self.menu_background, (0, 0))
