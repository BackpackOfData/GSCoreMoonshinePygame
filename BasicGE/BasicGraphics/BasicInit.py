# coding=utf-8

import pygame

class AppInit (object):

    def __init__(self):
        self.__display_resolution = (320, 200)
        self.__caption = u''
        self.__fpsCLC = pygame.time.Clock()




    def set_display(self, display):
        if type(display) is tuple:
            self.__display_resolution = display
            screen = pygame.display.set_mode(display)
            return screen
        else:
            raise TypeError('resolution touple needed')

    def get_display(self):
        return self.__display_resolution

    def set_caption(self, caption):
        if type(caption) is str or type(caption) is unicode:
            self.__caption = caption
        else:
            raise TypeError('caption - str or unicode needed')

    def get_caption(self):
        return self.__caption

    def set_tick(self, fps):
        self.__fpsCLC.tick(fps)

    def get_fps(self):
        return self.__fpsCLC.get_fps()

    def game_init(self):
        pygame.display.set_caption(self.__caption)
        pygame.init()
