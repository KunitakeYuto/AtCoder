N=int(input())
List = [list(input()) for i in range(N)]
def Change(List,i,j,N):
    if i-1>=0 and j-1>=0:
        if List[i-1][j-1]!=".":
            List[i-1][j-1]="X"
    if i-1>=0:
        if List[i-1][j]!=".":
            List[i-1][j]="X"
    if i-1>=0 and j+1<(2*N-1):
        if List[i-1][j+1]!=".":
            List[i-1][j+1]="X"
    return List
i=N-1
while i>=0:
    j=0
    while 2*N-1>j:
        if List[i][j]=="X":
            List=Change(List,i,j,N)
        j+=1
        
    i-=1
for k in List:
    print("".join(k))