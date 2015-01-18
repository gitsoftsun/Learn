#coding=utf-8
# python 中所有参数, -传引用

#function defination is here
def printStr(str):
	"print str"
	str = "change value in function";
	print str;
	return;
#you can call printStr function
str = "Hello";
print str;
printStr(str);

#function defination
def printInfo(name, age):
	"print info"
	print "My name is : %s, I'm %d years!" %(name, age);
	return;

#call printinfo function

printInfo("lzy", 23);
#命名参数
printInfo(age=22, name="lll");
#缺省参数- 在定义的时候, 给定初始值
#例如:
def printM(name="lll", age=2):
	"缺省参数"
	print name, age;
	return;
#call function
printM();
#不定长参数
#function defination
def printSomeInfo(*varTuple):
	"print some info"
	for var in varTuple:
		print var;
	return;
#call 
printSomeInfo("lzy", 23, "ZJU");
printSomeInfo();
printSomeInfo([23, "Hello"]);

#anonymous function defination
sum = lambda arg1, arg2: arg1+arg2;
#call function 
print "the value of total : ", sum(12, 3);
print "the sum of values : ", sum(1, 2);
result = lambda arg1, arg2, arg3: (arg1+arg2)%arg3;
#call result function
print "result is : ", result(2, 2, 2);