import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
    
    def triangle(self):
        UP = 1
        DIRECTION = UP
        forward = pygame.Vector2(0, DIRECTION).rotate(self.rotation)
        right = pygame.Vector2(0, DIRECTION).rotate(self.rotation + 90) * self.radius / 2
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)