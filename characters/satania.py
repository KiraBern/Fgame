import pygame
from PIL import Image
import picture.picture_pillow
from picture.picture_pillow import Pic_pil
from config.settings import Settings


class Satania:
    def __init__(self, ai_game):
        """инициализация корабля и задание eго стартовой позиции"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """Загрузка изображения и получение его rect"""

        # self.im = Image.open('picture/satania_sprite.bmp')
        # self.picture_satania = self.im.crop(self.settings.pic_pil01)
        # self.picture_satania.save('satania_stay01.bmp', quality=95)
        # self.image = pygame.image.load(self.picture_satania)
        self.image = pygame.image.load('picture/satania_stay.bmp')

        self.rect = self.image.get_rect()

        """каждый новый герой стартует с позиции..."""
        self.rect.midleft = self.screen_rect.midleft

        """сохранение значения позиции корабля"""
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # индикаторы движения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # индикаторы действий
        self.shot_indi = False

    def update(self):

        self._update_pic_satania()  # обновление изображения сатании

        """
        обновить текущю позицию сатании на основе индикатора движения
        """

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.satania_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.satania_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.satania_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.satania_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def _update_pic_satania(self):
        if self.shot_indi == True:  # если выстрел то меняем текстуру
            self.image = pygame.image.load('picture/satania_shot.bmp')
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
        if self.shot_indi == False:
            self.image = pygame.image.load('picture/satania_stay.bmp')
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

    def blitme(self):
        """отрисовка  в её теперишнем местоположении"""
        self.screen.blit(self.image, self.rect)
