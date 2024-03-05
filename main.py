
"""
TODO

- reposition level1
- make player larger?
- change to the next level on game win if there are more levels
- create level2
- make level1 winable

- stylize lava
- stylize star
- stylize surfaces

- make text appear for game over
- add text before the level starts (LVL 1)
- make player flip when changing directions

"""

import pygame
from assets.colors import *
from background import Background
from level import *
from player import Player
import pygame.mixer

#Game Settings
FPS=60
GRAVITY=1
SCREEN_WIDTH=1920
SCREEN_HEIGHT=1080

def game_lost(screen):
    #load text
    text_font = pygame.font.SysFont("Pixel Craft", 1000)
    game_over_text = text_font.render('Game Over. You Lose.', True, (0, 0, 0))
    screen.blit(game_over_text, (100, 400))
    #load sound
    pygame.mixer.music.load("assets/sounds/Super_Mario_64_Burn_SFX.wav")
    pygame.mixer.music.play()
    pygame.display.update()
    pygame.time.delay(3000)
    #quit game
    pygame.quit()

def game_win():
    print('Game Over. You Win!')
    pygame.quit()

def main():
    pygame.init()
    pygame.mixer.init()

    #Setup Game Window
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Panda Platformer")
    
    #Player Object
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT, x=0, y=0)

    #Level Object
    levels = Levels()
    levels.current_level = 0
    levels.add_level(level1)
    
    #Background Image
    background = Background(screen)

    #Background Music
    pygame.mixer.music.load("assets/sounds/sleep_it_off.wav")
    pygame.mixer.music.play(-1)
    
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
        for lava in levels.current_level.lava:
            if player.lavaCollisions(lava):
                game_lost(screen)
        for star in levels.current_level.stars:
            if player.starCollisions(star):
                game_win()
        for surface in levels.current_level.surfaces:
            player.surfaceCollisions(surface)
        
        #Screen Updates (order determines layer)
        background.draw_bg(player)
        levels.current_level.draw(screen)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit() 

if __name__ == '__main__':
    main()