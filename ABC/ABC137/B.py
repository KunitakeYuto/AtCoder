K, X = map(int, input().split())
List=[]
i=X-K+1
while i<=X+K-1:
    if i < -1000000 or i>1000000:
        pass
    else:
        List.append(i)
    i+=1
print(*List)