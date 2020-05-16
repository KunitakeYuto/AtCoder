N=int(input())
ans=0
i=1
while i<=N:
    if not len(str(i))%2==0:
        ans+=1
    i+=1
print(ans)