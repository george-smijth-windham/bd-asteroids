import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

VERSION = pygame.version.ver


def main():
    print(
        f"Starting Asteroids with pygame version: {VERSION}",
        f"Screen width: {SCREEN_WIDTH}",
        f"Screen height: {SCREEN_HEIGHT}",
        sep="\n",
    )


if __name__ == "__main__":
    main()
