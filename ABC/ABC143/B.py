import itertools
N=int(input())
List = list(map(int, input().split()))
ans=0
for i in itertools.permutations(List, r=2):
    ans+=(i[0]*i[1])
print(int(ans/2))