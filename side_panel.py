import pygame

class Button():
    def __init__(self, x, y, image, click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.click = click

    def draw(self, surface):
        self.action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.action = True
                if self.click:
                    self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        surface.blit(self.image, self.rect)

        return self.action