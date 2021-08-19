# coding: utf-8
import pygame


class BasicMouse(object):

    def __init__(self):
        super(BasicMouse, self).__init__()

    @staticmethod
    def get_mousepos():
        return pygame.mouse.get_pos()

    @staticmethod
    def get_pressed():
        return pygame.mouse.get_pressed()

    @staticmethod
    def set_mouse_visible(isVisible):
        return pygame.mouse.set_visible(isVisible)

class BasicCursor (object):
    def __init__(self):
        print 'cursor class here'