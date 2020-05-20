N,K = map(int, input().split())
List = list(map(int, input().split()))
i=1
cnt=0
while i<N:
    i+=(K-1)
    cnt+=1
print(cnt)