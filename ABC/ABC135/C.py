N=int(input())
AList = list(map(int, input().split()))
BList = list(map(int, input().split()))
Asum=sum(AList)
i=0
while i<N:
    Amari=max(0,BList[i]-AList[i])
    AList[i]=max(AList[i]-BList[i],0)
    AList[i+1]=max(AList[i+1]-Amari,0)
    i+=1
print(Asum-sum(AList))