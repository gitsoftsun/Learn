# coding=utf-8
# test exception pythons
def StringToInt(var):
	try:
		return int(var);
	except ValueError, e:
		print 'ValueError : ', e;
	else:
		print '当没有错误的时候会执行的'
	finally:
		print '无论什么时候都会执行的'

def causeExp():
	try:
		raise "raise Error";
	except Exception, e:
		print "exception ", e;
	else:
		print "这个不可能执行"
	finally:
		print '一定执行'

#call convert
# print StringToInt('9');
causeExp();