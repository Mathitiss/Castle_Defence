import pygame
import sys

class CastleDefence():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 820))

        pygame.display.set_caption("Castle Defence")
        pygame.display.flip()

    def run_game(self):
        while True:
            self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

    def keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()



if __name__ == "__main__":
    cd = CastleDefence()
    cd.run_game()