# -*- coding: utf-8 -*-

def fabonacci(num):
	'''
		@param num >= 2
		@return list
	'''
	reslut = [0, 1]
	for x in xrange(num-2):
		reslut.append(reslut[-2] + reslut[-1])
	return reslut

if __name__ == '__main__':
	print fabonacci(1)