#!/bin/usr/env python3
# -*- coding: utf-8 -*-

weight = float(input("体重(KG): "))
height = float(input("身高(M): "))

res = weight/(height * height)

if res > 38:
    mes = "太重了"
elif res > 25:
    mes = "还好"
elif res > 18:
    mes = "管肚子"
else:
    mes = '不错'

print('身高: %s ,\n体重: %s ,\nBMI: %s, 测算结果是: %s\n' % (height, weight, res, mes));