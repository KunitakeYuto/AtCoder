N=int(input())
List=input()
AList=list(List)
RCNT=AList.count("R")
BList=sorted(List)
ANUM=0
BNUM=0
ans=0
i=0
while i<N:
    if AList[i]!=BList[i]:
        ans+=1
    i+=1
print(ans//2)