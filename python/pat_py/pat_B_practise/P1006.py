# encoding=utf-8
__author__ = 'lzy'

inputNum = raw_input()
# steps : 解析每位数字是多少, 然后在进行循环打印
listNum = []
for i in reversed(range(0, 3)):
    listNum.append(int(int(inputNum) / pow(10, i)))
    inputNum = int(inputNum) % pow(10, i)
# print listNum
result = ""
if listNum[0] != 0:
    for j in range(0, listNum[0]):
        result += 'B'
if listNum[1] != 0:
    for k in range(0, listNum[1]):
        result += 'S'
if listNum[2] != 0:
    for l in range(1, listNum[2]+1):
        result += str(l)
print result