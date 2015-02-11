# -*- coding: utf-8 -*-
__author__ = 'User19'

import urllib


def cbk(a, b, c):
    per = 100.0*a*b/c
    if per > 100:
        per = 100
    print '%.2f%%' %per


url = 'http://www.sina.com.cn'
local_path = 'd:\download\sina.html'
urllib.urlretrieve(url, local_path, cbk)