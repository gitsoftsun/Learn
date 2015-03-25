# -*- coding: utf-8 -*-
__author__ = 'Lzy_pc'

import Image
import pytesseract
import os
print pytesseract.image_to_string(Image.open(r'E:\code\Learn\python\test\exp.png'))
# if os.path.exists(r'E:\code\Learn\python\test\exp.png'):
#     print pytesseract.image_to_string(Image.open('E:\code\Learn\python\test\exp.png', mode='r'))

