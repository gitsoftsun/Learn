#coding=utf-8
__author__ = 'lzy'

SEPARATOR = " "
inputs = raw_input()
SpaceCount = inputs.count(SEPARATOR, 0, inputs.__len__())
list_inputs = inputs.split(SEPARATOR, SpaceCount)
aNum = list_inputs[0].count(list_inputs[1], 0, list_inputs[0].__len__())
bNum = list_inputs[2].count(list_inputs[3], 0, list_inputs[2].__len__())
sumAB =0
for i in range(0, aNum):
    sumAB += pow(10, i)*int(list_inputs[1])
for j in range(0, bNum):
    sumAB += pow(10, j)*int(list_inputs[3])
print sumAB