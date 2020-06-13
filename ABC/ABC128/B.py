N = int(input())
List = [list(input().split()) for i in range(N)]
ANS=List
for j in range(N):
    List[j][1]=int(List[j][1])
RList=sorted(List,reverse=True, key=lambda x: x[1])
RList.sort(key=lambda x: x[0])
for i in range(N):
    print((ANS.index(RList[i]))+1)