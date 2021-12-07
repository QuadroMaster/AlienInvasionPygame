import sys
import os
import pygame
import time

from settings import Settings
from ship import Ship
from bullet import Bullet


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

        self.bullets = pygame.sprite.Group()

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
            self.bullets.update()

            # Удаление снарядов, вышедших за край экрана
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            print(len(self.bullets))
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """реагирует на нажатие клавиш"""
        if pygame.key.get_pressed()[pygame.K_q]:
            print("\nquit 3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        pygame.mouse.set_visible(False)
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    os.environ["DISPLAY"] = ":0"  # ВАЖНО!!! Без этого не будет выводиться окно pygame-a при удалённном запуске
    ai = AlienInvasion()
    ai.run_game()
