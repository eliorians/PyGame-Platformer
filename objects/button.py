import pygame

class Button:
    def __init__(self, x, y, image, scale=1):
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        action = False

        # Get mouse pos
        pos = pygame.mouse.get_pos()

        # Check mouse is over button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.image, self.rect)

        return action

