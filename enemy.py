import pygame
from settings import Settings

class Enemy():
    def __init__(self, cd_game):
        self.screen = cd_game.screen
        self.screen_rect = cd_game.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.image.load('img//tank.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.settings.waypoints[0]

        self.x = int(self.rect.x)
        self.y = int(self.rect.y)

    def moving(self):
        self.rect.x += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)