import pygame

class Button:
    def __init__(self, x, y, image, screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):

        action = False

        #get mouse pos
        pos = pygame.mouse.get_pos()

        #check mouse is over button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        #Draw buttons on screen
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return action
