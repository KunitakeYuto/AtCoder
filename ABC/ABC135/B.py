N=int(input())
List = list(map(int, input().split()))
cnt=0
i=0
while i<N:
    if not List[i]==i+1:
        cnt+=1
    i+=1
if cnt<=2:
    print("YES")
else:
    print("NO")