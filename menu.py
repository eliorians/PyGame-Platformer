import pygame
from button import *
import sys

menu_background = "assets/PandaMainMenu.png"
play_button_img = "assets/playButt.png"
                                    
class Menu:

    def __init__(self, screen):
        self.screen = screen
        play_button_img = pygame.image.load("assets/playButt.png").convert_alpha()
        play_button = Button( 150, 150, play_button_img, self.screen)
        
    def draw(self, screen):
        pygame.draw.rect(screen, menu_background, )



    
