# -*- coding: utf-8 -*-
__author__ = 'Lzy_pc'
class Test0325:
    """
     Basic Python (2Edit)
    """

    def test_dict(self):
        """
        测试 字典类型， 一个key对应 ？个value
        :return:
        """
        names = {}
        names['li'] = {'zhaoyang'}
        names['li'].add('shuran')  # dict可变类型mapping类型
        print names['li']

if __name__ == '__main__':
    test = Test0325()
    test.test_dict()