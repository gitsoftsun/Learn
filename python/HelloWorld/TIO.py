#coding=utf-8
# Test python input/output

#call formal function
# input1 = raw_input("Enter your name:");
# print "This is your name : ", input1;

#another input function
# input2 = input("Enter correct expression : ");
# print input2;

#open a file by open function
# content = open("test.txt", "wb");
# print "Name of the file : ", content.name;
# print "Closed or not: ", content.closed;
# print "Opening mode : ", content.mode;
# print "Softspace flag : ", content.softspace;

#write something to file bu function of the write
content = open("test1.txt", "r+");
# if not content.closed:
	# content.write("你好, 世界!\r\n python is a great language. Yeah its great!\n");
# content.close();

#read some bytes from test1.txt
subContent = content.read(10);
print "from test1.txt read some content : ", subContent;
content.close();
