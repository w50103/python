#!/usr/bin/env python3
# -*- coding:utf8 -*-

'图片处理类'
from PIL import Image, ImageFilter


def img():

    im = Image.open('name.jpg')
    print(im.format, im.size, im.mode)

    im.filter(ImageFilter,);
    im.save('filter.jpg','JPEG');

    im.thumbnail((200,100))
    im.save('thumb1.jpg','JPEG')

if __name__ == '__main__':
    img()
