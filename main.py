from textwrap import fill
import pygame
from constants import *
from player import Player
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock  
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color = "black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        #limit framerate to 60fps
        dt = clock.tick(60) / 1000
        
        


if __name__ == "__main__":
    main()
