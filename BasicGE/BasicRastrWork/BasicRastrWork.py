# coding=utf-8

import PIL.Image as IPIL
import pygame

class BasicImgEdit (object):
    def __init__(self, path):
        self.img = IPIL.open(path)
        self.size = self.img.size

    # Вырезка спрайта или тайла из картинки или атласа
    def cut_image(self, startposX, startposY, width, height):
        cutted = self.img.crop((startposX, startposY, startposX+width, startposY+height))
        return pygame.image.frombuffer(cutted.tobytes(), cutted.size, cutted.mode)

    # Конвертирование в self.Surface. Да, да, можно и по другому, но это ж PIL!
    def convert_to_surface(self):
        mode = self.img.mode
        size = self.img.size
        data = self.img.tobytes()
        return pygame.image.frombuffer(data, size, mode)

    # Статика, "посмотреть картинку", открвыем и смотрим на что мы там наделали
    # file = ImgClass ('file.png')
    # file.show (file.cut_image)
    @staticmethod
    def show(img):
        img.show()
