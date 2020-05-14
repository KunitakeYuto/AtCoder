N=int(input())
S=input()

if len(S)==1:
    print("No")
elif len(S)%2==0:
    A=N/2
    MAE=S[:int(A)]
    B=N/2
    USHIRO=S[int(B):]
    if MAE==USHIRO:
        print("Yes")
    else:
        print("No")
else:
    print("No")
    

