# -*-coding: utf-8 -*-
__author__ = 'Lzy_pc'

import Image
import pytesseract


def test_convert_img_str():
    """
    将图形验证码转化为字符串
    :return:
    """
    img = Image.open("exp.png")
    characters = pytesseract.image_to_string(img)
    print characters


def test_show_img():
    img = Image.open("exp.png")
    img.show()

if __name__ == '__main__':
    # test_show_img()
    test_convert_img_str()