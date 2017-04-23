#!/usr/bin/env python3
# -*- coding: utf8 -*-

def main():
    print(is_palindrome.__name__);
    print(list(filter(lambda x: str(x)==str(x)[::-1], range(1,100))))
    print(list(filter(is_palindrome,range(1,1000))));

def is_palindrome(n):

    n = str(n)
    return n == n[::-1]
if __name__ == '__main__':
    main()