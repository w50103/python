#!/usr/bin/env python3
# -*- coding: utf8 -*-
'template style'
import logging


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("name: %s, score %s" %(self.name, self.score))



if __name__ == '__main__':
    logging.exception('abcd')
    pass