N=int(input())
List = list(map(int, input().split()))
AList=[0]
cnt=0
i=0
while i<N:
    if i==0:
        Mae=List[0]
    elif i==N-1 and List[i]<=Mae:
        AList.append(cnt+1)
    elif i==N-1:
        AList.append(cnt)
    elif List[i]<=Mae:
        Mae=List[i]
        cnt+=1
    else:
        AList.append(cnt)
        Mae=List[i]
        cnt=0
    i+=1
print(max(AList))