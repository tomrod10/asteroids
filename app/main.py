import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # closes window/quits game
                return

        screen.fill((0, 0, 0))  # fills frame with RGB/A color
        pygame.display.flip()  # update contents of the whole display
        dt = clock.tick(60) / 1000  # limits frames to 60 fps


if __name__ == "__main__":
    main()
