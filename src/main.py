import sys
import pygame
from asteroids.src.constants import *
from asteroids.src.player import Player
from asteroids.src.asteroid import Asteroid
from asteroids.src.asteroidfield import AsteroidField
from asteroids.src.shot import Shot 
from asteroids.src.drawtext import draw_text


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    game_state = "MENU"
    paused = False

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if game_state == "MENU":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = "PLAYING"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused

        if game_state == "MENU":
            # Draw Menu Screen
            draw_text(screen, "ASTEROIDS", 100, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50)
            draw_text(screen, "Press SPACE to Start", 50, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)
            pygame.display.flip()
            continue
        if not paused:
            updatable.update(dt)


            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    print("Game over!")
                    sys.exit()

            for shot in shots:
                for asteroid in asteroids:
                    if asteroid.collides_with(shot):
                        shot.kill()
                        new_asteroids = asteroid.split()
                        for new_asteroid in new_asteroids:
                            asteroids.add(new_asteroid)
                            updatable.add(new_asteroid)
                            drawable.add(new_asteroid)
                        break  # Exit asteroid loop after hit
                        

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        if paused:
            draw_text(screen, "PAUSED", 100, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            draw_text(screen, "Press 'P' to Resume", 40, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 70)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()