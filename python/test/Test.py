# -*- coding: utf-8 -*-
__author__ = 'Lzy_pc'
# python 用正则表达式进行匹配的时候， 都是只能匹配开头符合正则表达式的字符（无法匹配字符串中间符合条件的字符串），若头部不能满足那么就不满足这不科学
# Question :
#   desc: python正则无法匹配字符串中间符合正则的字符串
import re


def test_re():
    pattern = re.compile('hello', re.I)
    match = pattern.match('Hello world')
    print match
    if match:
        print match.group()


def test_simple_re():
    """
   purpose: 匹配中间的数字
   question desc: python正则无法匹配字符串中间符合正则的字符串
    :return:
    """
    match = re.match(r'\d+', 'r123st')
    if match:
        print match.group()
        # real result : None
        # expect result : 123


def test_alias_re():
    m = re.match('(?P<id>\d)abc', '1abc')
    if m:
        print m.string
        print 'group alias is : ', m.groupdict('id')
        print m.groups()


def test_compile_flag():
    pattern = re.compile('\d+', re.U)
    match = pattern.match('r23sd')
    if match:
        print match.groups()


def match_iter():
    match = re.match(r'\w{1}', 'adfd')
    if match:
        print match.groups()


def test_search():
    m = re.search('\d+', 'rw2343fds')
    if m:
        print m.group()

if __name__ == '__main__':
    # test_simple_re()
    # test_alias_re()
    # test_compile_flag()
    # match_iter()
    test_search()