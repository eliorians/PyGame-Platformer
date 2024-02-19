
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
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
FPS=60
GRAVITY=3

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
    player_is_moving = False

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
        
        current_time = pygame.time.get_ticks()
        #Player Controls
        if keys[pygame.K_a]:
            player.move_left()
            player_is_moving = True
        if keys[pygame.K_d]:
            player.move_right(SCREEN_WIDTH, SCREEN_HEIGHT)
            player_is_moving = True
        if keys[pygame.K_w]:
            player.jump()
        
        #Passive Player things
        #player.update(SCREEN_HEIGHT)
        player.apply_gravity(GRAVITY)
        player.update_animation(clock.tick(FPS) / 1000.0)    
  
        #Player/Object collisions
        #screen
        player.screenCollisions(SCREEN_WIDTH, SCREEN_HEIGHT)
        #surfaces
        player.surfaceCollisions(surface)
        #lava
        if player.lavaCollisions(lava):
            game_lost()

        #Background Stuff
        #background.draw(screen)
        #background.update(player_is_moving)
        screen.fill(black)

        #Screen Updates (order determines layer)
        surface.draw(screen)
        lava.draw(screen)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == '__main__':
    main()