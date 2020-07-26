N,K = map(int, input().split())
AList = list(map(int, input().split()))
A=str(K)
i=int(A)
j=0
while j<=N-K:
    #BList=AList[j:i]
    if j==0:
        MAE=AList[j]
    elif MAE>=AList[i-1]:
        print("No")
        MAE=AList[j]
    elif MAE<AList[i-1]:
        print("Yes")
        MAE=AList[j]
    i+=1
    j+=1