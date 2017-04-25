#!/usr/bin/env python3
# -*- coding: utf8 -*-
'template style'
from orm.field import Field


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        print('Found Model : %s' % name)

        mappings = dict();

        for k,v in attrs.items():
            if isinstance(v, Field):
                print('Found mappings : %s==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name ,bases, attrs)