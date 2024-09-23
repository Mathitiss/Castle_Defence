import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2
import math

class Enemy(Sprite):
    def __init__(self, cd_game):
        super().__init__()
        self.screen = cd_game.screen
        self.screen_rect = cd_game.screen.get_rect()
        self.angle = 90

        self.image = pygame.image.load('img//tank.bmp')
        self.trans_image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()

        self.waypoints = [(100, 100), (400, 200), (400, 100), (200, 300)]
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2
        self.rect.center = self.pos

        self.x = int(self.rect.x)
        self.y = int(self.rect.y)

    def moving(self):
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            self.kill()
        
        self.distance = self.movement.length()
        if self.distance >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if self.distance != 0:
                self.pos += self.movement.normalize() * self.distance
            self.target_waypoint += 1

        # self.rect.center = self.pos

    def rotation(self):
        self.distance = self.target - self.pos
        self.angle = math.degrees(math.atan2(-self.distance[1], self.distance[0]))

        self.image = pygame.transform.rotate(self.trans_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    # def update(self):
    #     self.rect.x = self.x