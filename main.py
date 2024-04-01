
"""
TODO

LEVELS
- correct game over screen
- create level2
- level1 flow into level2

FEATURES
- lives
- add text before the level starts (LVL 1)
- make player flip when changing directions
- menu (option to change screen size - 2x screen size = 2x player size/speed/jump)

STYLING
- stylize lava
- stylize star
- stylize surfaces
- Background for different levels

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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def reset_level():
    # You should reset any variables or parameters related to the level's state here
    # For example:
    # reset character position
    character_position = (100, 100)
    # reset other level-specific variables
    
    # return the reset level state
    return character_position  # You can return other variables if needed


def game_lost(screen):
    # Fill the screen with white color

    level_state = reset_level()
    

    screen.fill((0, 0, 0))
    
    # Load text with variable size for the first page
    text_font = pygame.font.SysFont("Pixel Craft", 50)
    game_over_text = text_font.render('Game Over. You Lose.', True, (255, 255, 255))
    
    # Load text with variable size for the second page
    text_font = pygame.font.SysFont("Pixel Craft", 50)
    second_page_text = text_font.render('Press Enter to Restart.', True, (255, 255, 255))
    
    # Get the dimensions of the screen
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    
    # Calculate the center coordinates for the first page text
    game_over_text_x = (screen_width - game_over_text.get_width()) / 2
    game_over_text_y = (screen_height - game_over_text.get_height()) / 2
    
    # Calculate the center coordinates for the second page text
    second_page_text_x = (screen_width - second_page_text.get_width()) / 2
    second_page_text_y = game_over_text_y + game_over_text.get_height() + 20  # Add some space between the two messages
    
    # Blit the first page text to the screen at the calculated center coordinates
    screen.blit(game_over_text, (game_over_text_x, game_over_text_y))
    
    # Blit the second page text to the screen at the calculated center coordinates
    screen.blit(second_page_text, (second_page_text_x, second_page_text_y))
    
    pygame.display.flip()  # Update the display
    
    


    #load sound
    pygame.mixer.music.load("assets/sounds/Super_Mario_64_Burn_SFX.wav")
    pygame.mixer.music.play()
    pygame.display.update()
    pygame.time.delay(3000)
    #quit game
      
      # Wait for the user to press Enter to restart the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return level_state  # Exit the function to restart the game



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