S=input()

def count_diff2(q, a):
    return sum(
        c1 != c2 for c1, c2 in zip(q, a)
    )


if len(S)%2==0:
    Cut=int((len(S))/2)
    MAE=S[:Cut]
    USHIRO=S[-(Cut):]
    USHIRO=USHIRO[::-1]
    
    if MAE==USHIRO:
        print(0)
        quit()
    
    print(count_diff2(MAE,USHIRO))
    quit()

else:
    Cut=int((len(S))//2)
    MAE=S[:Cut]
    USHIRO=S[-(Cut):]
    USHIRO=USHIRO[::-1]
    
    if MAE==USHIRO:
        print(0)
        quit()
    
    print(count_diff2(MAE,USHIRO))
    quit()



