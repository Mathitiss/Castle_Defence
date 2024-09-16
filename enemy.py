import pygame

class Enemy():
    def __init__(self, cd_game):
        self.screen = cd_game.screen
        self.screen_rect = cd_game.screen.get_rect()

        self.image = pygame.image.load('img//tank.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = int(self.rect.x)
        self.y = int(self.rect.y)

    def moving(self):
        self.rect.y -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)