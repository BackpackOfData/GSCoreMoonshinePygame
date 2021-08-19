# coding:utf-8

'''

    Спрайты добавление в словарь тайлов и спрайтов
    в уровневом спрайте есть ошибочка поэтому позиция забита последняя
    для возврата необходимо вернуть self.lvl

'''

from BasicGE.BasicRastrWork import *
from BasicGE.BasicGraphics.BasicObject import *
from BasicGE.BasicCLvl.ConstructParser import *


class LoadSpritesToDict(object):
    '''
    Загрузка спрайтов и возврат их в виде списка.
    '''
    def __init__(self, parcedlvlf):
        self.__dictTile = {}
        self.__lvl = LvlFileParce(parcedlvlf).retStruct()

        for key in self.__lvl['init']:
                if self.__lvl['init'][key][0] == 'tLoad':
                    if len(self.__lvl['init'][key][1:]) == 6:
                        uncut = BasicImgEdit(self.__lvl['init'][key][1])
                        try:
                            cutted = uncut.cut_image(
                                            self.__lvl['init'][key][2],
                                            self.__lvl['init'][key][3],
                                            self.__lvl['init'][key][4],
                                            self.__lvl['init'][key][5])
                        except:
                            raise IOError("Wrong string format! " + self.__lvl['init'][key])
                        obj = GraphicObject(0, 0, 10, 10)
                        obj.set_surface(cutted)
                        try:
                            self.__dictTile[key] = [obj, self.__lvl['init'][key][6]]
                        except:
                            raise IOError("Wrong string format! " + self.__lvl['init'][key])
                    elif len(self.__lvl['init'][key][1:]) == 2:
                        si = GraphicObject (0, 0, 10, 10)
                        si.load_image(self.__lvl['init'][key][1])
                        try:
                            self.__dictTile[key] = [si, self.__lvl['init'][key][2]]
                        except:
                            raise IOError("Wrong string format! " + self.lvl['init'][key])
    def ret_tile_dict (self):
        return self.__dictTile


class CreateTileMap:
    def __init__(self, lvlfile):
        self.__dictTile = {}
        self.__lvl = LvlFileParce(lvlfile).retStruct()['lvl']
        self.__parce_lvl_file()

    def ret_lvl_dict(self):
        return self.__dictTile

    def __parce_lvl_file(self):
        for string in self.__lvl:
            string = string.replace(';', '')
            for every_tile in string.split(','):
                match = re.match('([a-zA-Z][a-zA-Z0-9]*)\[(((\d+)[-](\d+))|(\d+))\]', every_tile)
                print match.group(1), match.group(4), match.group(5), match.group(6)

