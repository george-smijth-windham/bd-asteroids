import sys
import pygame
from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHOT_RADIUS,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            # self.shot_cooldown_timer -= dt

    def move(self, dt):
        vector = pygame.Vector2(0, 1)
        rotate_vector = vector.rotate(self.rotation)
        speed_vector = rotate_vector * PLAYER_SPEED * dt
        self.position += speed_vector

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        # print(self.shot_cooldown_timer)
        # sys.exit()
        # print(self.shot_cooldown_timer)
        # sys.exit()
        # return
        # if self.shot_cooldown_timer:
        #     return
        # self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        vector = pygame.Vector2(0, 1)
        rotate_vector = vector.rotate(self.rotation)
        shot.velocity = rotate_vector * PLAYER_SHOOT_SPEED
        # shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        # shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        # vector = pygame.Vector2(0, 1)
        # rotate_vector = vector.rotate(self.rotation)
        # speed_vector = rotate_vector * PLAYER_SHOOT_SPEED
        # shot.position += speed_vector
