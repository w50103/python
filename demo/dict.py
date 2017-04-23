#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dictionary = {'abc':123,'bcd':456, 'cde':345}

for key in dictionary:
    print('%s\n' % dictionary[key])


myset = set([1,2,3,4,5,6])

n=10

while(n > 0):
    if (n%2 ==0):
        myset.add(n)
    else:
        pass

    n = n-1


print(myset);