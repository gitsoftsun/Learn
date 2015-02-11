# -*- coding: utf-8 -*-
__author__ = 'User19'

# 有序数组A和B的交集
import random


def mixed(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            c.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    return c


def main():
    lst = list(range(10))
    a = sorted(random.sample(lst, 4))
    b = sorted(random.sample(lst, 5))
    print '%s \n%s' %(a, b)
    print 'A B mixed'
    # print mixed(a, b)
    print set(a) & set(b)  # 交集
    print set(a) | set(b)  # 并集
    print set(a) - set(b)  # 差集
    print set(a) ^ set(b)  # 对称差集（只存在A或者B集合中）
if __name__ == '__main__':
    main()