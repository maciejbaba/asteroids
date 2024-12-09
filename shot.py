import pygame
from circleshape import CircleShape
from constants import PLAYER_BULLET_SPEED, PLAYER_BULLET_RADIUS, WHITE

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, PLAYER_BULLET_RADIUS)
        self.velocity = velocity * PLAYER_BULLET_SPEED

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius)

