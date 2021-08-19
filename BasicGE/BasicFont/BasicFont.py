# coding=utf-8
# Basic Font Work



from BasicGE.BasicGraphics import *


class TextInit (object):
    def __init__(self):
        pygame.font.init()

    def close_font_init (self):
        pygame.font.quit()


class FontWork (pygame.font.Font):

    def __init__(self, name, size):
        super(FontWork, self).__init__(name, size)
        self.__color = (255, 0, 0)
        self.__lines = []
        self.__antialias = 0


    def set_color (self, color):
        self.__color = color

    def set_antialias (self, antialias):
        self.__antialias = antialias

    def set_text(self, text):
        self.__lines = text.split(u'\n')
        self.__lines = filter(None, self.__lines)

    def set_lines (self, lines):
        if type (lines) is list:
            self.__lines = lines
        else:
            raise ValueError('Lines in text dialog must be a list!')

    def get_lines(self):
        return self.__lines

    def __get_surfaces(self):
        if len(self.__lines) <= 1:
            return self.render(self.__lines[0], self.__antialias, self.__color)
        else:
            surf_collector = []
            for line in self.__lines:
                surf_collector.append(self.render (line, self.__antialias, self.__color))
            return surf_collector

    '''
    Выравнивание текста идет по первой строке будьте внимательны!
    '''
    def render_align_center(self, text, x,y):
        self.set_text(text)
        surf = self.__get_surfaces()
        obj_listz = []
        if type (surf) is list:
            center = 0
            for z, s in enumerate(surf):
                    w,h = s.get_size()
                    if z == 0:
                        gO= GraphicObject(x,y+h*z, w,h, self.__color)
                        center = gO.rect.center
                    else:
                        gO = GraphicObject(x, y + h * z, w, h, self.__color)
                        gO.rect.center = center[0],y + h * z+h/2
                    gO.set_surface(s)
                    obj_listz.append(gO)
            return obj_listz
        elif type(surf) is pygame.Surface:
            w,h = surf.get_size()
            gO = GraphicObject(x,y, w, h, color=self.__color)
            gO.set_surface(surf)
            return gO

    def render_lign_left(self, text, x,y):

        self.set_text(text)
        surf = self.__get_surfaces()
        obj_listz = []
        if type(surf) is list:
            center = 0
            for z, s in enumerate(surf):
                w, h = s.get_size()
                gO = GraphicObject(x, y + h * z, w, h, self.__color)
                gO.set_surface(s)
                obj_listz.append(gO)
            return obj_listz

        elif type(surf) is pygame.Surface:
            w, h = surf.get_size()
            gO = GraphicObject(x, y, w, h, color=self.__color)
            gO.set_surface(surf)
            return gO

    def render_lign_right(self, text, x, y):
        self.set_text(text)
        surf = self.__get_surfaces()
        obj_listz = []
        if type(surf) is list:
            right = 0
            for z, s in enumerate(surf):
                w, h = s.get_size()
                if z == 0:
                    gO = GraphicObject(x, y + h * z, w, h, self.__color)
                    right = gO.rect.right
                else:
                    gO = GraphicObject(x, y + h * z, w, h, self.__color)
                    gO.rect.right = right
                gO.set_surface(s)
                obj_listz.append(gO)
            return obj_listz
        elif type(surf) is pygame.Surface:
            w, h = surf.get_size()
            gO = GraphicObject(x, y, w, h, color=self.__color)
            gO.set_surface(surf)
            return gO


