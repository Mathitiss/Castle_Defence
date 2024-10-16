import pygame

class Level():  #!
    def __init__(self, map_image, side_img):
        self.image = map_image
        self.side = side_img

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        surface.blit(self.side, (1198, 0))