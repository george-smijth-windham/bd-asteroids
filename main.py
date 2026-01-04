import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

VERSION = pygame.version.ver


def main():
    print(
        f"Starting Asteroids with pygame version: {VERSION}",
        f"Screen width: {SCREEN_WIDTH}",
        f"Screen height: {SCREEN_HEIGHT}",
        sep="\n",
    )
    num_pass, num_fail = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
