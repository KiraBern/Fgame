import pygame
from PIL import Image
from config.settings import Settings





class Pic_pil:
    def __init__(self):


        self.im = Image.open('satania_sprite.bmp')
        self.picture_satania = self.im.crop(self.settings.pic_pil01)
        self.picture_satania.save('pic_pil011.bmp')
        self.picture_satania.show()
