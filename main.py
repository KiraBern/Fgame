import sys
import pygame

from bullets.bullet_standart import Bullets1
from config.settings import Settings
from characters.satania import Satania


class FGame:
    def __init__(self):
        pygame.init()  # инициализация стартовых настроек pygame
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)  # задаём размер окна
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("FGame")  # название окна?

        self.satania = Satania(self)  # импорт сатании
        self.bullets = pygame.sprite.Group()

        # задание цвета фона
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Главный цыкл игры"""
        while True:
            """слежка за мышкой и клавой"""
            for event in pygame.event.get():

                if event.type == pygame.QUIT:  # закрыть игру если нажата кнопка закрывания
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.satania.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.satania.moving_left = True
                    if event.key == pygame.K_UP:
                        self.satania.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.satania.moving_down = True
                    elif event.key == pygame.K_BACKSPACE:
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        new_bullet = Bullets1(self)
                        self.bullets.add(new_bullet)

                elif event.type == pygame.KEYUP:
                    if event.key ==pygame.K_RIGHT:
                        self.satania.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.satania.moving_left = False
                    if event.key == pygame.K_UP:
                        self.satania.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.satania.moving_down = False


            """Обновление состояния корабля"""
            self.satania.update()
            self.bullets.update()
            """заново перерисовать экран на каждой итерации цикла"""
            self.screen.fill(self.settings.bg_color)
            self.satania.blitme()  # отрисовка сатании
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            """Показ последний нарисованый екран"""
            pygame.display.flip()


if __name__ == '__main__':
    ai = FGame()
    ai.run_game()
