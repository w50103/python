#!/usr/bin/env python3
# -*- coding: utf8 -*-
'template style'
import re
import urllib
from urllib import request

with request.urlopen('http://weather.yahooapis.com/forecastrss?u=c&w=2151330') as f:
    data = f.read()

    print('Status:', f.status, f.reason)

    for k,v in f.getheaders():
        if re.match(r'.*?Cookie$',k):
            print('%s : %s' % (k,re.split(r'[\s|\;]+',v)))
        else:
            pass
   # print('Data:',data.decode('utf-8'))