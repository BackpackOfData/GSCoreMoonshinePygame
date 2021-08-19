# coding=utf-8

# Basic PyGame Group

import pygame

# Объединение спрайтов в группу,  остальное из pygame.sprite.Group


class UniteSprite(pygame.sprite.Group):
    def __init__(self, *sprites):
        super(UniteSprite, self).__init__()
        self.add(sprites)
