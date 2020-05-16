N=int(input())
List = list(map(int, input().split()))
Max=0
i=0
while i<N:
    if List[i]-Max <= -2:
        print("No")
        quit()
    Max=max(Max,List[i])
    i+=1
print("Yes")