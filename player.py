import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
        self.width = 2
        self.shot_cooldown = 0
    
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
        pygame.draw.polygon(screen, WHITE, self.triangle(), self.width)
    
    def move(self, dt):
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shot_cooldown > 0:
            return
        Shot(self.position, pygame.Vector2(0, 1).rotate(self.rotation))
        self.shot_cooldown = PLAYER_SHOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()
        right = dt
        left = -dt

        self.shot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(right)
        
        if keys[pygame.K_d]:
            self.rotate(left)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
