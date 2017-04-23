#!/usr/bin/env python3
# -*- coding: utf8 -*-
import math

def myfunction(param1, param2):
    print("param1 is %s, param2 is %s" %(param1,param2))

    return 'nb';


def my_abs( n):
    if not isinstance(n, (float,int)):
        raise TypeError("bad opend type")

    if n >=0:
        return n
    else:
        return -n


def checkType(n, type):
    if ((type == 'string' )or (type == 'str')):
        if not isinstance(n, str):
            raise TypeError("you should user str")
    elif (type == "number" or type == "num"):
        if not isinstance(n, (float,int)):
            raise TypeError("you shoule use num")
    else:
        print(" param n is checkparma, type: [str,string,num,number]")


    return 'success';

def quadratic(a,b,c):
    if(checkType(a, 'num') and checkType(b, 'num') and checkType(c, 'num')):
        print("%sx + %sx + %s" % (a,b,c))
        sqNum = b*b - 4*a*c;
        x1 = (-b + math.sqrt(sqNum))
        x2 = -b - math.sqrt(sqNum)

        return x1,x2
    else:
        pass


