N=int(input())
B=list(map(int, input().split()))
ANS=0
i=0
while i<N:
    if i==0:
        ANS+=B[i]
        mae=B[i]
    elif i==N-1:
        ANS+=mae
    else:
        ANS+=min(B[i],mae)
        mae=B[i]
    i+=1
print(ANS)