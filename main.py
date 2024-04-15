
"""
TODO

ESSENTIAL
- fin level2
- each person design their own lvl...

STYLING
- stylize lava / surface (simple and static?)
- make player flip when changing directions

NEW FEATURES
- lives
- menu settings (turn off music/sfx)
- store that sells hats (doesnt affect hitbox)
- dumplings that you can grab & shoot to damage enemies

"""

import pygame
import pygame.mixer
from level import *
from objects.button import Button
from player import *
from assets.colors import *
from objects.menu import *
from objects.background import *

#Game Settings
FPS=60
GRAVITY=1
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    '''
    Sets up the game and loads the main menu. 
    Different actions occur depending on the button pressed.
    '''
    pygame.init()
    pygame.mixer.init()

    #Setup Game Window
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Panda Platformer")
    
    #Player Object
    player = Player(x=0, y=0)

    #Levels List & each Level Object
    levels = Levels()
    levels.add_level(level1)
    levels.add_level(level2)
    levels.add_level(level3)
    
    #Background Image (currently used in all levels...)
    background = Background(screen, "assets/Jungle Asset Pack/parallax background", 0)

    #Menu Instantiation
    menu = Menu(screen)

    #Main Menu Button Instantiation
    play_button_img = pygame.image.load("assets/playButt.png").convert_alpha()
    quit_button_img = pygame.image.load("assets/quitButt.png").convert_alpha()

    play_button = Button(530, 150, play_button_img)
    quit_button = Button(530, 300, quit_button_img)

    #Menu Music
    pygame.mixer.music.load("assets/sounds/noodle cove.wav")
    pygame.mixer.music.play(-1)
    
    while True:
        #Load Menu and Buttons
        menu.draw()
        play_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.update()

        #Menu Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif play_button.draw(screen):
                mainGameLoop(screen, clock, player, levels, background)
            elif quit_button.draw(screen):
                pygame.quit()

            
        
def mainGameLoop(screen, clock, player, levels, background):
    '''
    The main game loop.
    '''
    #if the current level has been displayed
    showLevelName = False

    while True:

        #Display the Current Level
        if not showLevelName:
            screen.fill((0, 0, 0)) 
            text_font = pygame.font.SysFont("Pixel Craft", 100)
            text = text_font.render(f'Level: {levels.current_level_index}', True, (255, 255, 255))
            screen.blit(text, ((SCREEN_WIDTH - text.get_width()) / 2, (SCREEN_HEIGHT - text.get_height()) / 2))
            pygame.display.update()
            pygame.time.delay(1000)
            showLevelName = True

        #Game Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                main()
            elif event.type == pygame.KEYDOWN:
                #Exit Game w/ Escape
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    main()
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

        #Update Enemies
        for enemy in levels.current_level.enemy:
            enemy.update()

        #Player/Object Collisions
        for lava in levels.current_level.lava:
            if player.lavaCollisions(lava):
                level_lost(screen)
        for star in levels.current_level.stars:
            if player.starCollisions(star):
                level_win(levels, player)
                showLevelName = False
        for bamboo in levels.current_level.bamboo:
            if player.bambooCollisions(bamboo):
                player.upgrade_jump()
                bamboo.here = True
        for surface in levels.current_level.surfaces:
            player.surfaceCollisions(surface)
                
        #Screen Updates (order determines layer)
        background.draw_bg(player)
        levels.current_level.draw(screen)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
    
def level_win(levels, player):
    '''
    Result of player collecting the star in a level (win).
    '''
    #check if there are more levels available
    if levels.current_level_index + 1 < len(levels.level_list):
        #increment the current level index
        levels.current_level_index += 1
        #move player back to start
        player.reset_position()
    else:
        print('Congratulations! You have completed all levels!')
        pygame.quit()
        main()

def level_lost(screen):
    '''
    Result of player dying in a level (lose).
    '''
    #black background
    screen.fill((0, 0, 0))
    #create text
    text_font = pygame.font.SysFont("Pixel Craft", 100)
    text = text_font.render('Game Over. You Lose.', True, (255, 255, 255))
    #position text
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    text_x = (screen_width - text.get_width()) / 2
    text_y = (screen_height - text.get_height()) / 2
    #draw
    screen.blit(text, (text_x, text_y))
    #load sound
    pygame.mixer.music.load("assets/sounds/Super_Mario_64_Burn_SFX.wav")
    pygame.mixer.music.play()
    pygame.display.update()
    pygame.time.delay(3000)
    #quit game
    pygame.quit()
    main()

if __name__ == '__main__':
    main()