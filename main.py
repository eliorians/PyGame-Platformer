
#todo fix surfaces (character seems to float on it)
#todo use levels to build objects instead of in main


#todo stylize lava and surfaces
#todo make player flip when changing directions

import pygame
from assets.colors import *
from player import Player
from lava import Lava
from surface import Surface
from star import Star
from background import Background

#Game Settings
FPS=60
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
GROUND_HEIGHT=30
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
    pygame.display.set_caption("Panda Platformer")
    
    #Create Objects
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT, x=0, y=0)
    surface1 = Surface(x=0, y=SCREEN_HEIGHT-GROUND_HEIGHT, height=GROUND_HEIGHT, width=SCREEN_WIDTH)
    surface2 = Surface(x=250, y=500, height=GROUND_HEIGHT, width=250)
    lava = Lava(x=300, y=SCREEN_HEIGHT-GROUND_HEIGHT, height=GROUND_HEIGHT, width=250)
    star = Star(x=750, y=550, height= 10, width=10)
    
    #Background stuff
    background = Background(screen)
    
    #Main Game Loop
    gameRunning = True

    while gameRunning:

        #Game Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
            elif event.type == pygame.KEYDOWN:
                #Exit Game w/ Escape
                if event.key == pygame.K_ESCAPE:
                    gameRunning = False
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
  
        #Update Player
        player.update(GRAVITY, clock.tick(FPS) / 1000.0, SCREEN_WIDTH, SCREEN_HEIGHT)    

        #Player/Object Collisions
        #lava
        if player.lavaCollisions(lava):
            game_lost()
        #star
        if player.starCollisions(star):
            game_win()
        #surfaces
        player.surfaceCollisions(surface1)
        player.surfaceCollisions(surface2)
        
        #Background Stuff
        #screen.fill(black)
        background.draw_bg(player)

        #Screen Updates (order determines layer)
        surface1.draw(screen)
        surface2.draw(screen)
        lava.draw(screen)
        star.draw(screen)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit() 

if __name__ == '__main__':
    main()