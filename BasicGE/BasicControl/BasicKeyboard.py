#coding= utf-8

import pygame

class BasicKeyboard (object):

    def __init__(self):
        super(BasicKeyboard, self).__init__()

    @staticmethod
    def get_keyname(event):
        return pygame.key.name(event)

    @staticmethod
    def get_keypressed():
        return pygame.key.get_pressed()