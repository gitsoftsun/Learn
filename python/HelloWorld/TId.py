#coding=utf-8
#测试   身份运算符  is是判断两个标识符是不是引用自一个对象
# a = 10; b =10; a is b ?
a = 10; b = 10;
print a is b
b = 20
# 改变b 的值, 结果是 : false
print a is b