
"""
TODO

- flex playe
- change to the next level on game win if there are more levels
- create level2
- make level1 winable
- Make level 2 occur once star is grabbed and then add new bkg

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

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

def game_lost(screen):
    # Fill the screen with white color
    screen.fill((0, 0, 0))
    
    # Load text with variable size
    text_font = pygame.font.SysFont("Pixel Craft", 150)
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

def level_win():
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
    
    #Background Image (takes image path, and level num)
    background = Background(screen, "assets/Jungle Asset Pack/parallax background", 0)

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
                level_win()
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