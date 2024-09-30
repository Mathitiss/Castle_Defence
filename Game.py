import pygame
import sys
from settings import Settings
# from castle import Castle      НА БУДУЩЕЕ (castle под ship)
from enemy import Enemy
from map import Level
from turret import Turret

class CastleDefence():
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.map_image = pygame.image.load('img//level.png')
        self.map = Level(self.map_image)
        # self.castle = Castle(self)    НА БУДУЩЕЕ (castle под ship)

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()    
        pygame.display.set_caption("Castle Defence")

        self.enemy_group = pygame.sprite.Group()
        self.create_enemy()
        self.cursor_turret = pygame.image.load('img//turret.png')
        self.turret_group = pygame.sprite.Group()

        self.draw = pygame.draw
        
    def run_game(self):
        while True:
            self.events()
            self.enemy_move()
            self.enemy_update()
            self.update_screen()  
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_pos = pygame.mouse.get_pos()
                self.turret = Turret(self.cursor_turret)
                self.turret_group.add(self.turret)

    def keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def create_enemy(self):
        self.enemy = Enemy(self)
        self.enemy_group.add(self.enemy)

    def enemy_move(self):
        self.enemy.moving()
        self.enemy.rotation()

    def enemy_update(self):
        self.enemy_group.update()

    def update_screen(self):
        self.screen.fill('grey')
        # self.castle.blitme()    НА БУДУЩЕЕ (castle под ship)
        self.map.draw(self.screen)

        self.enemy_group.draw(self.screen)
        self.turret_group.draw(self.screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    cd = CastleDefence()
    cd.run_game()