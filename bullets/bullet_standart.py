import pygame
from pygame.sprite import Sprite
from config.settings import Settings


class Bullets1(Sprite):
    """класс управления стандартными снарядами"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # создать rect снаряда в 0,0 и задать правильное положение
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.satania.rect.midtop    # !!!!!!!!!!!!возможная ошибка

        # Сохранение позиции снаряда как десятичное значение
        self.x = float(self.rect.x)

    def update(self):
        """сдвинуть снаряд """
        self.x += self.settings.bullet_speed
        """обновить позицию rect"""
        self.rect.x = self.x

    def draw_bullet(self):
        """отрисовка снаряда"""
        pygame.draw.rect(self.screen, self.color, self.rect)
