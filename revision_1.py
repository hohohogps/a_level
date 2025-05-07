import math
#https://www.codewars.com/kata/51edd51599a189fe7f000015/solutions/python
def Mean_Squared_Error(array_a, array_b):
    return sum((i[0] - i[1])**2 for i in list(zip(array_a, array_b))) / len(array_a)
#https://www.codewars.com/kata/523d2e964680d1f749000135/train/python
def interleave(*args):
    res = []
    for j in range (max(len(t) for t in args)):
        for i in range (len(args)):
            if j <= len(args[i])-1:
                res.append(args[i][j])
            else:
                res.append(None)
    return res