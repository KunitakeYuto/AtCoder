N=int(input())
S=input()
ans=1
i=0
while i<N:
    if i==0:
        MAE=S[i]
    else:
        if S[i]==MAE:
            MAE=S[i]
            pass
        else:
            MAE=S[i]
            ans+=1
    i+=1
print(ans)