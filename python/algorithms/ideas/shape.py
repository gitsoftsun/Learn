# -*- coding: utf-8 -*-
__author__ = 'lzy'


def print_grid():
    """
     打印7×7的方格
    :return:
    """
    for i in range(8):
        line_r = ' '
        for j in range(7):
            line_r += '-'
            if j != 7:
                line_r += ' '
        print line_r
        line_c = ''
        if i == 7:
            return
        for k in range(8):
            line_c += '|'
            if k != 7:
                line_c += ' '
        print line_c


def main():
    print_grid()

if __name__ == '__main__':
    main()