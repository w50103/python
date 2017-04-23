#!/usr/bin/env python3
# -*- coding: utf8 -*-


'我是注释，看看对不对'

__author__ = "Neo Zhou"

import sys;

def test():
    args = sys.argv

    if len(args) == 1:
        print("Hello World!!!")
    elif len(args) == 2:
        print("Hello World , %s" % args[1])
    else:
        print("Too Many Arguments!!!")
if __name__ == '__main__':
    test();