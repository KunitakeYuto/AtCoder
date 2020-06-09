N,L=map(int, input().split())
List=[]
i=1
while i<=N:
    List.append(L+i-1)
    i+=1
MIN=abs(List[0])
HIKU=List[0]
j=1
while j<N:
    if abs(List[j])<MIN:
        HIKU=List[j]
        MIN=abs(List[j])
    j+=1
del List[List.index(HIKU)]
print(sum(List))