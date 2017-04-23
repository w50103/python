#!/usr/bin/env python3
# -*- coding: utf8 -*-

from os import listdir
from functools import reduce


# definer

# 位置参数

def power(n, m=2):
    res = 1
    while m > 0:
        res = res * n
        m = m - 1

    return res


def register(name, age, city='beijin', gender='m'):
    print("Name is %s, age is %s, city is %s, gender is %s" % (name, age, city, gender))


def stradd(l=None):
    if l is None:
        l = []
    l.append('END')
    return l


def cale(numbers):
    sums = 0

    for n in numbers:
        sums += n * n

    return sums


def calenew(*numbers):
    res = 0
    for n in numbers:
        res += n * n

    return res


def kwparam(name, gender, **kw):
    print('name is', name, 'gender is ', gender, 'other is ', kw)


def kwcity(name, gender, *, city, province):
    print('name :', name, 'gender:', gender, 'city:', city, 'province:', province)


def pathful(path='.'):
    for p in [d for d in listdir(path)]:
        print('%s \n' % p)


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[s]

    return reduce(fn, map(char2num, s))


def str2label(s):
    def fn(x,y):
        return x + y

    def char2num(s):
        return {"0":"零","1":"一","2":"二","3":"三","4":"四","5":"五","6":"六","7":"七","8":"八","9":"九"}[s]


    return reduce(fn,map(char2num,s))


def normalize(name):
    return name[0:1].upper() + name[1:].lower()
    pass

def mystrip(s):
    return s and s.strip()


def _init_odd():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisable(n):
    return lambda x: x%n > 0

def primes():
    yield 2

    it = _init_odd()

    while True:
        n = next(it)
        yield n
        it = filter(_not_divisable,it)

def main():
    for n in primes():
        if n < 100000:
            print(n)
        else:
            break


if __name__ == '__main__':
    main()
# user
