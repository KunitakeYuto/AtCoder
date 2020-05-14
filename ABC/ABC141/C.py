N,K,Q = map(int, input().split())
List = [int(input()) for i in range(Q)]
PList=[K-Q]*N
for i in range(0,Q):
    PList[(List[i])-1]+=1
for j in range(0,N):
    if PList[j]>0:
        print("Yes")
    else:
        print("No")