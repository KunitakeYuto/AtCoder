N=int(input())
AList = list(map(int, input().split()))
BList = list(map(int, input().split()))
CList = list(map(int, input().split()))
mae=0
MAN=0
i=0
while i<N:
    MAN+=BList[(AList[i])-1]
    if (mae+1)==AList[i] and i!=0:
        MAN+=CList[mae-1]
    mae=AList[i]
    i+=1
print(MAN)