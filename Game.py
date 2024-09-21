import pygame
import sys
from settings import Settings
# from castle import Castle      НА БУДУЩЕЕ (castle под ship)
from enemy import Enemy

class CastleDefence():
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()    
        pygame.display.set_caption("Castle Defence")

        # self.castle = Castle(self)    НА БУДУЩЕЕ (castle под ship)

        self.enemy_group = pygame.sprite.Group()  # Group, add, kill, remove
        self.create_enemy()

        self.draw = pygame.draw   # WHO ???
        
    def run_game(self):
        while True:
            self.events()
            self.create_enemy()
            self.enemy_move()
            self.enemy_update()
            self.draw_lines()
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

    def create_enemy(self):
        self.enemy = Enemy(self)
        self.enemy_group.add(self.enemy)

    def enemy_move(self):
        self.enemy.moving()     

    def enemy_update(self):
        self.enemy_group.update()

    def draw_lines(self):
        self.draw.lines(self.screen, "red", False, self.enemy.waypoints)

    def update_screen(self):    # Скорее всего под enemy нужно сделать цикл, а это оставить под castle !!!
        self.screen.fill('grey')
        # self.castle.blitme()    НА БУДУЩЕЕ (castle под ship)
        self.draw.lines(self.screen, "red", False, self.enemy.waypoints)

        self.enemy_group.draw(self.screen)

        pygame.display.flip()

if __name__ == "__main__":
    cd = CastleDefence()
    cd.run_game()