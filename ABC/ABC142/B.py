N,K = map(int, input().split())
List = list(map(int, input().split()))
ans=0
i=0
while i<N:
    if List[i]>=K:
        ans+=1
    i+=1
print(ans)