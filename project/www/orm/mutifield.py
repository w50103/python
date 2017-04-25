#!/usr/bin/env python3
# -*- coding: utf8 -*-
'template style'
from orm.field import Field


class StringField(Field):
    def __init__(self, name):
        super(StringField,self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')