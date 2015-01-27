# coding = utf-8
__author__ = 'lzy'

# http://www.patest.cn/submissions/1033672 miss one case
weights = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
tupM = (1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2)
in_Num = raw_input()
ins = []
inValidIns = []
for i in range(0, int(in_Num)):
    ins.append(raw_input())
for var in ins:
    var = str(var)
    for i in range(0, 17):
        if not var[i:i+1].isdigit():
            inValidIns.append(var)
            ins.remove(var)
            break
# print "inValid ins : ", len(inValidIns)
for v in ins:
    tmpSum = 0
    for i in range(0, 17):
        tmpSum += int(str(v)[i:i+1])*weights[i]
    result = tmpSum % 11
    if not str(v[17:]).__eq__(str(tupM[result])):
        inValidIns.append(v)
        # ins.remove(v)


if len(inValidIns) == 0:
    print 'All passed'
else:
    for vl in inValidIns:
        print vl


# define function


def is_num_by_exception(arg):
    """judge : is_Num_byException"""
    try:
        int(arg)
        return True
    except ValueError:
        return False
