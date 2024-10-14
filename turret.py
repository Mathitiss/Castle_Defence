import pygame
from settings import Settings

class Turret(pygame.sprite.Sprite):
    def __init__(self, image, tile_x, tile_y):
        pygame.sprite.Sprite.__init__(self)
        self.settings = Settings()

        self.tile_x = tile_x
        self.tile_y = tile_y

        self.x = (self.tile_x + 0.5) * self.settings.tile_size_x
        self.y = (self.tile_y + 0.5) * self.settings.tile_size_y

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)