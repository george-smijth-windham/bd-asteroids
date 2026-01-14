import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

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
    clock = pygame.time.Clock()
    running = True
    dt = 0
    # group = pygame.sprite.Group()
    # updatable, drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        # player.draw(screen)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # player.update(dt)
        updatable.update(dt)
    # pygame.quit()


if __name__ == "__main__":
    main()
