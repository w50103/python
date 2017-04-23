#!/usr/bin/env python3
# -*- coding: utf8 -*-
'template style'



class FmaleStudent(object):
    __slots__ = ('name','age');
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    #
    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name

    def setscore(self, score):
        if 0 <= score <=100:
            self.__score = score
        else:
            raise ValueError('err score')

    def print_names(self, *args, **kwargs):
        print(__doc__, *kwargs.items());

    def print_score(self):
        print("%s : %s" % (self.__name, self.__score))

class malStudent(FmaleStudent):
    def print_method(self):
        print(__class__)


