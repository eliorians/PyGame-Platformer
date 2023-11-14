
import pygame
import sys
import clock

from assets.colors import *

def main():
    pygame.init()

    #setup game window
    screen_width = 1920
    screen_height = 1080
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))
    fps = 60

    #setup player
    #player_image = pygame.image.load('assets/players/player_eli.png')
    #player_width, player_height = player_image.get_size()
    player_width = 100
    player_height = 100
    player_x = screen_width // 2 - player_width // 2
    player_y = screen_height - player_height - 10

    player_speed = 5
    player_jump_height = 5
    gravity = 2
    
    #main game loop
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()

        #move left
        if keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        #move right
        if keys[pygame.K_d] and player_x < screen_width - player_width:
            player_x += player_speed
        #jump
        if keys[pygame.K_w]:
            player_y -= player_jump_height
            
        #gravity
        player_y += gravity

        #edge collison detection
            #left edge
        if player_x < 0:
            player_x = 0
            #right edge
        elif player_x > screen_width - player_width:
            player_x = screen_width - player_width
            #bottom edge
        if player_y < 0:
            player_y = 0
            #top edge
        elif player_y > screen_height - player_height:
            player_y = screen_height - player_height

        #screen updates
        screen.fill(black)
        #screen.blit(player_image, (player_x, player_y))
        pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()

if __name__ == '__main__':
    main()