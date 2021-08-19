# coding=utf-8

import re

class LvlFileParce(object):
    def __init__(self, file):
        try:
            self.gentile = open(file, 'r')
        except:
            raise IOError('file does not exist')
        self.__objPrepare = self.__parse()

    def __parse(self):
        lvl_struct = {}
        key = ''
        for line in self.gentile:
            line = line.replace(' ', '').replace('\n','').replace('\t', '')
            if line is not '':
                if line [0] != '{' and line[-1] != '}':
                    if line [0] == '!':
                        lvl_struct [line [1:]] = []
                        key = line [1:]
                    else:
                        lvl_struct[key].append(line)

        variablestruct = {}
        struct_Ex = {}
        line_count = 0
        line_tiles = {}
        for key in lvl_struct.keys():
            for line in lvl_struct[key]:
                if line.find ('=tLoad') != -1:
                    struct_prepare = re.match("(.+)=(tLoad)\('(.*)\',([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+)\);", line)
                    if struct_prepare is None:
                        struct_prepare = re.match("(.+)=(tLoad)\('(.*)\',([0-9]+)\);", line)
                        if struct_prepare is not None:
                            variablestruct[struct_prepare.group(1)] = [struct_prepare.group(2), struct_prepare.group(3), int (struct_prepare.group(4))]
                    else:
                        variablestruct[struct_prepare.group(1)] = [struct_prepare.group(2),struct_prepare.group(3), int(struct_prepare.group(4)),
                                                                   int(struct_prepare.group(5)), int(struct_prepare.group(6)),
                                                                   int(struct_prepare.group(7)), int(struct_prepare.group(8))]
                    lvl_struct[key] = variablestruct

                elif line.find ('=sLoad') != -1:

                    struct_prepare = re.match("(.+)=(sLoad)\('(.*)\',([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+)\);",
                                              line)
                    if struct_prepare is None:
                        struct_prepare = re.match("(.+)=(sLoad)\('(.*)\',([0-9]+)\);", line)
                        if struct_prepare is not None:
                            variablestruct[struct_prepare.group(1)] = [struct_prepare.group(2), struct_prepare.group(3),
                                                                       int(struct_prepare.group(4))]
                    else:
                        variablestruct[struct_prepare.group(1)] = [struct_prepare.group(2),
                                                                   struct_prepare.group(3),
                                                                   int(struct_prepare.group(4)),
                                                                   int(struct_prepare.group(5)),
                                                                   int(struct_prepare.group(6)),
                                                                   int(struct_prepare.group(7)),
                                                                   int(struct_prepare.group(8))]
                    lvl_struct[key] = variablestruct
                #script execute parce
                elif line.find ('.Execute') != -1:
                    match = re.match('([a-zA-Z0-9]+)\.(Execute)\(([0-9]+),([0-9]+)\);',line)
                    struct_Ex[match.group(1)] = [match.group(2), match.group(3), match.group(4)]
                    lvl_struct[key] = struct_Ex

                #map parce
                elif re.match('([a-zA-Z][a-zA-Z0-9]*)\[(\d+)-(\d+)\]', line) is not None:
                    line_tiles[str(line_count)] = line.replace(';','')
                    line_count +=1

                else:
                    raise SyntaxError('Raise LVL FILE DEAD in variables : '+line)

        return lvl_struct

    def retStruct(self):
        return self.__objPrepare

