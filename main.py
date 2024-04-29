
"""
TODO

ESSENTIAL
- presentation

STYLING
- make player flip when changing directions

NEW FEATURES
- lives
- menu level select
- menu settings (turn off music/sfx)
- store
"""

import pygame
import pygame.mixer
from level import *
from player import *
from assets.colors import *
from objects.menu import *
from objects.button import Button
from objects.background import *

#Game Settings
FPS=60
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
    levels.add_level(level4)
    levels.add_level(level5)

    #Background Image (currently used in all levels...)
    background = Background(screen, "assets/Jungle Asset Pack/parallax background", 0)

    #Menu Instantiation
    menu = Menu(screen)

    #Variable to keep track if you are in the store
    inStore = False

    #Main Menu Button Instantiation
    play_button_img = pygame.image.load("assets/playButt.png").convert_alpha()
    quit_button_img = pygame.image.load("assets/quitButt.png").convert_alpha()
    store_button_img = pygame.image.load("assets/storeButt.png").convert_alpha()
    # Load color button images and scale them
    new_width = 200
    new_height = 200
    red_button_img = pygame.transform.scale(pygame.image.load("assets/redButton.png").convert_alpha(), (new_width, new_height))
    rainbow_button_img = pygame.transform.scale(pygame.image.load("assets/rainbowButton.png").convert_alpha(), (new_width, new_height))
    white_button_img = pygame.transform.scale(pygame.image.load("assets/whiteButton.png").convert_alpha(), (new_width, new_height))
    yellow_button_img = pygame.transform.scale(pygame.image.load("assets/yelllowButton.png").convert_alpha(), (new_width, new_height))

    play_button = Button(530, 150, play_button_img)
    quit_button = Button(530, 425, quit_button_img)
    store_button = Button(75, 200, store_button_img)
   
    red_button = Button(575, 350, red_button_img, 1)
    rainbow_button = Button(575, 75, rainbow_button_img, 1)
    white_button = Button(400, 350, white_button_img, 1)
    yellow_button = Button(400, 75, yellow_button_img, 1)

    #Menu Music
    pygame.mixer.music.load("assets/sounds/noodle cove.wav")
    pygame.mixer.music.play(-1)
    
    while True:
        #Load Menu and Buttons
        menu.draw()
        if not inStore:
            play_button.draw(screen)
            quit_button.draw(screen)
            store_button.draw(screen)
        else:  # You are in the store
            red_button.draw(screen)
            rainbow_button.draw(screen)  # draw the rainbow button in the store
            white_button.draw(screen)  # draw the white button in the store
            yellow_button.draw(screen)  # draw the yellow button in the store
        pygame.display.update()

        #Menu Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif inStore:
                if red_button.draw(screen):  # if red button is clicked
                    player.set_color('red')
                    inStore = False  # go back to the main menu
                elif rainbow_button.draw(screen):  # if rainbow button is clicked
                    player.set_color('rainbow')
                    inStore = False  # go back to the main menu
                elif white_button.draw(screen):  # if white button is clicked
                    player.set_color('white')
                    inStore = False  # go back to the main menu
                elif yellow_button.draw(screen):  # if yellow button is clicked
                    player.set_color('yellow')
                    inStore = False  # go back to the main menu
            else:
                if play_button.draw(screen):
                    inStore = False
                    mainGameLoop(screen, clock, player, levels, background)
                elif quit_button.draw(screen):
                    pygame.quit()
                elif store_button.draw(screen):
                    inStore = True
                    menu.draw()
                    pygame.display.update()

        
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
        player.update(clock.tick(FPS) / 1000.0, SCREEN_WIDTH, SCREEN_HEIGHT)   

        #Update Enemies
        for enemy in levels.current_level.enemy:
            enemy.update()

        #Player/Object Collisions
        for spikes in levels.current_level.spikes:
            if player.spikesCollisions(spikes):
                level_lost(screen)
        for lava in levels.current_level.lava:
            if player.lavaCollisions(lava):
                level_lost(screen)
        for enemy in levels.current_level.enemy:
            if player.enemyCollisions(enemy):
                level_lost(screen)
        for star in levels.current_level.stars:
            if player.starCollisions(star):
                level_win(screen, levels, player)
                showLevelName = False
        for bamboo in levels.current_level.bamboo:
            if player.bambooCollisions(bamboo):
                if bamboo.here == False:
                    bamboo.here = True
                    player.upgrade_jump()
        for surface in levels.current_level.surfaces:
            player.surfaceCollisions(surface)
        for moon in levels.current_level.moon:
            if player.moonCollisions(moon):
                if moon.here == False:
                    moon.here = True
                    player.flipGravity()
       
        #Screen Updates (order determines layer)
        background.draw_bg(player)
        levels.current_level.draw(screen)
        player.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
    
def level_win(screen, levels, player):
    '''
    Result of player collecting the star in a level (win).
    '''
    #check if there are more levels available
    if levels.current_level_index < len(levels.level_list):
        #increment the current level index
        levels.current_level_index += 1
        #move player back to start
        player.reset_player()
    else:
        #black background
        screen.fill((0, 0, 0))
        #create text
        text_font = pygame.font.SysFont("Pixel Craft", 100)
        text = text_font.render('Game Over. You Win!', True, (255, 255, 255))
        #position text
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        text_x = (screen_width - text.get_width()) / 2
        text_y = (screen_height - text.get_height()) / 2
        #draw
        screen.blit(text, (text_x, text_y))
        #wait and quit
        pygame.display.update()
        pygame.time.delay(3000)
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
    text = text_font.render('Game Over. You Lose!', True, (255, 255, 255))
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