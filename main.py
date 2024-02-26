
#TODO
# 1) fix jumps
# 2) fix surface objects

# 3) add star objects
# 4) stylize background/lava
# 5) use levels to build objects instead of in main

import pygame
from assets.colors import *
from player import Player
from lava import Lava
from background import ParallaxBackground
from surface import Surface

#Game Settings
FPS=60
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
GRAVITY=1

def game_lost():
    print('Game Over. You Lose.')
    pygame.quit()

def game_win():
    print('Game Over. You Win!')
    pygame.quit()

def main():
    pygame.init()

    #Setup Game Window
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Create Objects
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    surface = Surface(x= 300, y=500, height=25, width=50)
    lava = Lava(x=400, y=500, height=50, width=100)
    background = ParallaxBackground(SCREEN_WIDTH, SCREEN_HEIGHT)

    #Main Game Loop
    running = True

    while running:

        #Game Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                #Exit Game w/ Escape
                if event.key == pygame.K_ESCAPE:
                    running = False
                #Move Left
                elif event.key == pygame.K_a:
                    player.move_left()
                #Move Right
                elif event.key == pygame.K_d:
                    player.move_right()
                #Jump
                elif event.key == pygame.K_w:
                    player.jump()
            elif event.type == pygame.KEYUP:
                #stop moving when the A or D key is released
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player.stop_moving()
                #stop jumping when the W key is released
                if event.key == pygame.K_w:
                    player.is_jumping = False
  
        #Player/Object Collisions
        #surfaces
        player.surfaceCollisions(surface)
        #lava
        if player.lavaCollisions(lava):
            game_lost()

        #Update Player
        player.update(GRAVITY, clock.tick(FPS) / 1000.0, SCREEN_WIDTH, SCREEN_HEIGHT)    

        #Background Stuff
        #background.draw(screen)
        #background.update(player_is_moving)
        screen.fill(black)

        #Screen Updates (order determines layer)
        lava.draw(screen)
        surface.draw(screen)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == '__main__':
    main()