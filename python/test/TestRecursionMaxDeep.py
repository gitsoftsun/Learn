# -*- coding: utf-8 -*-
__author__ = 'Lzy_pc'

def recursionCount(n):
    if n <= 0:
        return
    print n
    recursionCount(n-1)
if __name__ == '__main__':
    recursionCount(1000)