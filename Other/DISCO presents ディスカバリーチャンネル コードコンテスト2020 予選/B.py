import numpy
import numpy as np
N=int(input())
AList=list(map(int,input().split()))
AListSum=sum(AList)
CumSum=list(numpy.cumsum(numpy.array(AList)))
def getNearestValue(List, num):
    idx = np.abs(np.asarray(List) - num).argmin()
    return idx
MAE=sum(AList[:(getNearestValue(CumSum, AListSum/2))+1])
USHIRO=sum(AList[(getNearestValue(CumSum, AListSum/2))+1:])
print(abs(MAE-USHIRO))