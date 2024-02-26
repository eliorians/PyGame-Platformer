
#todo stylize stuff
#todo use levels to build objects instead of in main

import pygame
from assets.colors import *
from player import Player
from lava import Lava
from background import ParallaxBackground
from surface import Surface
from star import Star

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
    pygame.display.set_caption("Panda Platformer")
    
    #Create Objects
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    surface = Surface(x= 300, y=450, height=30, width=300)
    lava = Lava(x=400, y=600, height=50, width=50)
    star = Star(x=550, y=600, height= 10, width=10)
    
    #Background stuff
    bg_images = []
    for i in range(1, 6):
        bg_image = pygame.image.load(f"assets/Jungle Asset Pack/parallax background/plx-{i}.png").convert_alpha()
        bg_images.append(bg_image)

    def draw_bg():
        for i in bg_images:
            screen.blit(i, (0, 0))
    
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
        player.surfaceCollisions(surface)
        
        #Background Stuff
        #screen.fill(black)
        draw_bg()

        #Screen Updates (order determines layer)
        lava.draw(screen)
        surface.draw(screen)
        star.draw(screen)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == '__main__':
    main()