#coding=utf-8

import os

# os.rename('test.txt', 'rename.pdf')

# os.rename('rename.pdf', 'renametotest.txt')

# os.remove('renametotest.txt')

#create a new folder
# os.mkdir('test')


#Error : AttributeError: 'NoneType' object has no attribute 'mkdir'
# os.mkdir('test1').mkdir('test2')

print 'my name is : %s, my age is %d' %('lll', 23);

#chdir() 

#output current file path
print os.getcwd();

#del folder test.txt
os.rmdir('test')

