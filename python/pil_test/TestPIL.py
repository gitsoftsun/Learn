# -*- coding: utf-8 -*-
__author__ = 'Lzy_pc'
from PIL import Image
import pytesseract


def test_read_image():
    """
    读取本地图片
    :return:
    """
    im = Image.open('../test/exp.png')
    im.show()


def identifyCode():
    """
    识别验证码
    :return:
    """
    image = Image.open('../test/exp.png')
    identify_code = pytesseract.image_to_string(image)
    print identify_code

if __name__ == '__main__':
    # test_read_image()
    identifyCode()