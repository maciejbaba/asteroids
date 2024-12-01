import pygame
from constants import *

pygame.init()

def main():
    print('Starting asteroids!')
    print('Screen width: ' + str(SCREEN_WIDTH))
    print('Screen height: ' + str(SCREEN_HEIGHT))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.Surface.fill(screen, (0, 0, 0))

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == '__main__':
    main()
