N=int(input())
List = list(map(int, input().split()))
List.sort()
ans=0
i=0
while i<N:
    if i==0:
        pass
        ans=List[i]
    else:
        ans=(List[i]+ans)/2
    i+=1
print(ans)