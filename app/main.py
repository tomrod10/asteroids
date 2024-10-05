import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # adds instance of player class to two groups
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # closes window/quits game
                return

        screen.fill((0, 0, 0))  # fills frame with RGB/A color
        for item in updateable:  # updates player movement
            item.update(dt)
        for item in drawable:  # draws sprites to screen
            item.draw(screen)
        pygame.display.flip()  # update contents of the whole display
        dt = clock.tick(60) / 1000  # limits frames to 60 fps


if __name__ == "__main__":
    main()
