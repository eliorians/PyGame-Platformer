
"""
TODO

HIGH PRIORITY
- fin level2 (add a bug that moves?)
- add text before the level starts (LVL 1)
- lives
- menu (start game, options, quit)
- stylize lava
- stylize star
- stylize surfaces

LOW PRIORITY
- make player flip when changing directions
- Add dumplings that you can grab & shoot
- Change music between menu & levels
- Add a store (why not?)

"""

import pygame
from assets.colors import *
from background import Background
from level import *
from player import Player
from menu import *
import pygame.mixer

#Game Settings
FPS=60
GRAVITY=1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def game_lost(screen):
    # Fill the screen with white color
    screen.fill((0, 0, 0))
    
    # Load text with variable size
    text_font = pygame.font.SysFont("Pixel Craft", 100)
    game_over_text = text_font.render('Game Over. You Lose.', True, (255, 255, 255))
    
    # Get the dimensions of the screen
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    
    # Calculate the center coordinates for the text
    text_x = (screen_width - game_over_text.get_width()) / 2
    text_y = (screen_height - game_over_text.get_height()) / 2
    
    # Blit the text to the screen at the calculated center coordinates
    screen.blit(game_over_text, (text_x, text_y))

    #load sound
    pygame.mixer.music.load("assets/sounds/Super_Mario_64_Burn_SFX.wav")
    pygame.mixer.music.play()
    pygame.display.update()
    pygame.time.delay(3000)
    #quit game
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
    levels.add_level(level1)
    levels.add_level(level2)
    
    #Background Image (takes image path, and level num)
    background = Background(screen, "assets/Jungle Asset Pack/parallax background", 0)

    #Menu Instantiation
    menu = Menu(screen)

    #Button Instantiation
    play_button_img = pygame.image.load("assets/playButt.png").convert_alpha()
    play_button = Button(530, 150, play_button_img)

    #Background Music
    pygame.mixer.music.load("assets/sounds/sleep_it_off.wav")
    pygame.mixer.music.play(-1)
    
    #Main Game Loop
    gameRunning = True
    inMenu = True

    while gameRunning:
        if inMenu:
            menu.draw()
            play_button.draw(screen)
            pygame.display.update()

            #Game Controls for menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameRunning = False
                elif play_button.draw(screen):
                    inMenu = False
        
        else:

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
                    levels.level_win(player)
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