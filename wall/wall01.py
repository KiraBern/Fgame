import pygame
from pygame.sprite import Sprite
from characters.satania import Satania



class Wall01 (Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.satania = Satania(self)

        self.image = pygame.image.load('wall/preview_108.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    # def update(self):
    #
    #     self.satania.moving_down = False



    def walus(self):
        """отрисовка  в её теперишнем местоположении"""
        self.screen.blit(self.image, self.rect)
