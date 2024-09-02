import pygame
import sys
from settings import Settings
# from castle import Castle
from enemy import Enemy

class CastleDefence():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()    

        pygame.display.set_caption("Castle Defence")

        self.enemy = Enemy(self)            # Скорее всего под enemy нужно сделать цикл, а это оставить под castle !!!
        self.enemy = pygame.sprite.Group()  # Скорее всего под enemy нужно сделать цикл, а это оставить под castle !!!
        
    def run_game(self):
        while True:
            self.events()
            self.update_screen()   
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

    def keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def update_screen(self):    # Скорее всего под enemy нужно сделать цикл, а это оставить под castle !!!
        self.enemy.blitme()
        self.enemy.draw(self.screen)

        pygame.display.flip()

if __name__ == "__main__":
    cd = CastleDefence()
    cd.run_game()