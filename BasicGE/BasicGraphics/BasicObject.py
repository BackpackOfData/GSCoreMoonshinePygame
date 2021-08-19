# coding=utf-8

import pygame


class GraphicObject(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color='#FF0000'):
        super(GraphicObject, self).__init__()
        self.image = pygame.Surface([width, height])
        if type(color) == str:
            self.color = pygame.Color(color)
        else:
            self.color = color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(self.color)

    def load_image(self, path_to_img):
        x, y = self.rect.x, self.rect.y
        self.image = pygame.image.load(path_to_img)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def change_color(self, color):
        self.image.fill(pygame.Color(color))

    def set_surface(self, surface):
        x, y = self.rect.x, self.rect.y
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def get_size(self):
        return self.image.get_size()

    def get_current_pos(self):
        return self.rect

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))