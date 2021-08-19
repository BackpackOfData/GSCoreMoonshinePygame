# coding = utf-8

import BasicGE

# Анимированный спрайт


class AnimatedObject(BasicGE.GraphicObject):
    def __init__(self, x, y, width, height, color='#00ff00'):
        super(AnimatedObject, self).__init__(x, y, width, height, color)
        # блок анимации
        self.anim_block = []
        # кадр анимации
        self.__clip = 0
        self.anim_dict = dict()

    # Создание списка анимаций ImgEditClass.cut_image
    def set_animation_list(self, *imglink):
        for img in imglink:
            self.anim_block.append(img)
        self.image = self.anim_block[0]

    def set_animation_dict (self, dict):
        self.anim_dict = dict

    def set_animation_dict_to_list(self, key):
        self.anim_block = self.anim_dict[key]

    def set_anim_element(self, imginlistcount):
        self.image = self.anim_block[imginlistcount]

    def ret_animblock(self):
        return self.anim_block

    # Анимация кадра для анимации необходимо запихнуть
    # эту функуцию в основной блок программы
    def animate(self):
        if self.__clip < len(self.anim_block):
            self.image = self.anim_block[self.__clip]
            self.__clip += 1
        else:
            self.__clip = 0

    # вернуть кадр - отладка и его номер
    def ret_clip(self):
        return self.__clip, self.anim_block[self.__clip]