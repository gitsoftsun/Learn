# -*- coding: utf-8 -*-
def returnDateType(data):
	'''
		方法的返回值类型，并没有确定； 那是否可以说是 一个方法可以返回好几种类型的数据呢？
	'''
	if isinstance(data, str):
		print '%s is str type\n' % data
	elif isinstance(data, int):
		print '%d is int type\n' % data
	elif isinstance(data, list):
		print '%s is the list type\n' % list
	else:
		print 'unknow type'

def loop():
	'''
		循环从3开始， 用python如何实现？
	'''
	for x in xrange(3,10):
		print x


if __name__ == '__main__':
	# loop()w
	returnDateType([0, 1])