import pygame
import sys
from settings import Settings
# from castle import Castle      НА БУДУЩЕЕ (castle под ship)
from enemy import Enemy
from map import Level
from turret import Turret
from side_panel import Button

class CastleDefence():
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.map_image = pygame.image.load('img//level.png')
        self.side_img = pygame.image.load('img//side_bar3.png') 
        self.map = Level(self.map_image, self.side_img)
        # self.castle = Castle(self)    НА БУДУЩЕЕ (castle под ship)

        self.screen = pygame.display.set_mode((self.settings.screen_width + self.settings.side_panel, self.settings.screen_height))
        self.clock = pygame.time.Clock()    
        pygame.display.set_caption("Castle Defence")

        self.enemy_group = pygame.sprite.Group()
        self.create_enemy()
        self.cursor_turret = pygame.image.load('img//turret.png')  
        self.turret_group = pygame.sprite.Group()

        self.buy_img = pygame.image.load('img//buy_btn.png') 
        self.cancel_img = pygame.image.load('img//cancel_btn.png')

        self.buy_button = Button(self.settings.screen_width + 80, 120, self.buy_img)
        self.cancel_button = Button(self.settings.screen_width + 100, 210, self.cancel_img)

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
                if self.mouse_pos[0] < self.settings.screen_width and self.mouse_pos[1] < self.settings.screen_height:
                    self.create_turret(self.mouse_pos)

    def keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def create_enemy(self):
        self.enemy = Enemy(self)
        self.enemy_group.add(self.enemy)

    def create_turret(self, mouse_pos):
        self.mouse_tile_x = mouse_pos[0] // self.settings.tile_size_x
        self.mouse_tile_y = mouse_pos[1] // self.settings.tile_size_y

        self.mouse_num = (self.mouse_tile_y * self.settings.cols) + self.mouse_tile_x 
        if self.settings.tile_map[self.mouse_num] == 1:
            self.free_space = True
            for turret in self.turret_group:
                if (self.mouse_tile_x, self.mouse_tile_y) == (turret.tile_x, turret.tile_y):
                    self.free_space = False
            if self.free_space:
                self.new_turret = Turret(self.cursor_turret, self.mouse_tile_x, self.mouse_tile_y)
                self.turret_group.add(self.new_turret)

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

        self.buy_button.draw(self.screen)
        self.cancel_button.draw(self.screen)

        pygame.display.flip()

if __name__ == "__main__":
    cd = CastleDefence()
    cd.run_game()