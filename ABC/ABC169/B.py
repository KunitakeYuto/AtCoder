N=int(input())
List = list(map(int, input().split()))
List=sorted(List)
List=List[::-1]
if List.count(0)!=0:
    print(0)
    quit()
ANS=List[0]
i=1
while i<N:
    ANS=ANS*List[i]
    if ANS>1000000000000000000:
        print(-1)
        quit()
    i+=1
print(ANS)