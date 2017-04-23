#!/usr/bin/env python3
# -*- coding: utf8 -*-
'template style'

class Screen(object):

    @property
    def width(self):
        return self.__width;

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('Value must be inter')

        self.__width = width

    @property
    def height(self):
        return self.___height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('Value must be int')

        self.__height = height