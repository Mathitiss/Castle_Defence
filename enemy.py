import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, cd_game):
        super().__init__()
        self.screen = cd_game.screen
        self.image = pygame.image.load('img//tank.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

'''
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.get.center = pos
'''
