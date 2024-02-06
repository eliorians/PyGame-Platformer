
import pygame

from assets.colors import *
from player import Player

#Game Settings
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
FPS=60
GRAVITY = 2

def main():
    pygame.init()

    #Setup Game Window
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Setup Player
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    #Main Game Loop
    running = True
    while running:
        
        #Exit Game (close window or esc key)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        #Detect keys
        keys = pygame.key.get_pressed()
        
        #Player Controls
        if keys[pygame.K_a]:
            player.move_left()
        if keys[pygame.K_d]:
            player.move_right(SCREEN_WIDTH, SCREEN_HEIGHT)
        if keys[pygame.K_w]:
            player.jump()
        
        #Passive Player things
        player.apply_gravity(GRAVITY)
        player.handle_collisions(SCREEN_WIDTH, SCREEN_HEIGHT)
        player.update_animation(clock.tick(FPS) / 1000.0)

        #Screen Updates (redraw screen and player)
        screen.fill(black)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == '__main__':
    main()