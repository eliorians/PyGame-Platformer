import pygame
import sys

class ParallaxBackground:
    def __init__(self, screen, images, speeds):
        """
        Initialize the parallax background.

        Parameters:
        - screen: Pygame screen surface
        - images: List of image paths for each layer (ordered from back to front)
        - speeds: List of scrolling speeds for each layer (ordered from back to front)
        """
        self.screen = screen
        self.images = [pygame.image.load(image).convert() for image in images]
        self.speeds = speeds
        self.num_layers = len(images)
        self.width, self.height = screen.get_size()
        self.scroll_x = [0] * self.num_layers

    def update(self):
        """
        Update the scroll positions based on the speeds.
        """
        for i in range(self.num_layers):
            self.scroll_x[i] = (self.scroll_x[i] + self.speeds[i]) % self.width

    def draw(self):
        """
        Draw the parallax background on the screen.
        """
        for i in range(self.num_layers):
            self.screen.blit(self.images[i], (self.scroll_x[i] - self.width, 0))
            self.screen.blit(self.images[i], (self.scroll_x[i], 0))

    def scroll(self, delta_x):
        """
        Manually scroll the background by a specified amount.

        Parameters:
        - delta_x: Amount to scroll in the x-direction
        """
        for i in range(self.num_layers):
            self.scroll_x[i] = (self.scroll_x[i] + delta_x) % self.width