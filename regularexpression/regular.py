#!/usr/bin/env python3
# -*- coding: utf8 -*-
'template style'

import re


if re.match(r'^1[3|5|7|8|4]\d{9}$', str(input("mobile:"))):
    print('是个手机号')

else:
    print('不是一个手机号呢')


splitstr = input('split:')

print('使用函数切割 %s, 使用正则切割 %s' % (splitstr.split(' '), re.split(r'[\s|\,|\;]+', splitstr) ))





