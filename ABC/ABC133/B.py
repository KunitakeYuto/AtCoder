import itertools
import math

def dist(a,b):
    res=0
    for i in range(D):
        res+=(abs(a[i]-b[i]))**2
    res=res**0.5
    return res

N,D = map(int, input().split())
List = [list(map(int, input().split())) for i in range(N)]

ans=0
for i in range(N-1):
    for j in range(i+1,N):
        if dist(List[i],List[j]).is_integer()==True:
            ans+=1

print(ans)
