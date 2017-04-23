#!/usr/bin/env python3
# -*- coding: utf8 -*-

def foo(s):
    '''
    Function to get devide of 10
    
    Example:
    
    >>> foo(1)
    10.0
    
    >>> foo(0)
    Traceback (most recent call last):
        ...
    AssertionError: n is zero!!!
  
    '''
    n = int(s)

    assert n !=0, 'n is zero!!!'

    return 10/n

def main():
    foo('0')


if __name__ == '__main__':
    import doctest
    doctest.testmod()