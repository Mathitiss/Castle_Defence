class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.ship = Ship(self)
        self.enemies = pygame.sprite.Group()

        self._create_fleet()

def run_game(self):
    while True:
        self._update_enemy()                    
        self._update_screen()


def _create_fleet(self):
    enemy = Enemy(self)

    enemy_width, enemy_heigh = enemy.rect.size
    available_space_x = self.settings.screen_width - (2 * enemy_width)
    number_enemy_x = available_space_x // (2 * enemy_width)

    ship_height = self.ship.rect.height
    available_space_y = (self.settings.screen_height - (3 * enemy_heigh) - ship_height)
    number_rows = available_space_y // (2 * enemy_heigh)
    
    for row_number in range(number_rows):
        for enemy_number in range(number_enemy_x):
            self._create_enemy(enemy_number, row_number)

def _create_enemy(self):
    enemy = Enemy(self)
    self.enemies.add(enemy)

def _update_enemy(self):
    self._check_fleet_edges()
    self.enemies.update()

def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()

    self.enemies.draw(self.screen)
        
    pygame.display.flip()