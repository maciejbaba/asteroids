import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()


def main():
    print("Starting asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.Surface.fill(screen, BLACK)

    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        dt = clock.tick(60) / 1000
        pygame.Surface.fill(screen, BLACK)

        for entity in updateable:
            entity.update(dt)

        for entity in drawable:
            entity.draw(screen)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                exit()
        


        pygame.display.flip()


if __name__ == "__main__":
    main()
