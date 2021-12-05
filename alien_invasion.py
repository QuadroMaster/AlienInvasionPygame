import sys
import os
import pygame
import time

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""
        pygame.display.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        """В книге было self.ship = Ship(screen), я поменял на self.ship = Ship(self.screen), а на форуме прочитал:
        Я полагаю, вы хотели, чтобы в строке self.ship = Ship(self.screen) говорилось self.ship = Ship(self). 
        Таким образом, объект Ship может получить доступ ко всем атрибутам объекта AlienInvasion, а не только 
        к его атрибуту screen (и этот атрибут не имеет атрибута screen, таким образом ошибка). ТО ЕСТЬ ОПЕЧАТКА- 
        ВМЕСТО self ОНИ НАПИСАЛИ screen"""

    def run_game(self):
        """Запуск основного цикла игры"""
        '''while True:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()'''
        while True:
            self._check_events()
            # При каждом проходе цикла перерисовывается экран
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_q]:
                    print("\nquit 3...")
                    time.sleep(1)
                    print("2...")
                    time.sleep(1)
                    print("1...")
                    time.sleep(1)
                    sys.exit()
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        '''Обновляет изображения на экране и отображает новый экран'''
        pygame.mouse.set_visible(False)
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    os.environ["DISPLAY"] = ":0"  # ВАЖНО!!! Без этого не будет выводиться окно pygame-a при удалённном запуске
    ai = AlienInvasion()
    ai.run_game()
