N=int(input())
List = list(map(int, input().split()))
AList = [0]*N
for i in range(0,N):
    S=List[i]
    AList[S-1]=i+1
print(*AList)