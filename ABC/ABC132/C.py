N=int(input())
List=list(map(int, input().split()))
List=sorted(List)
print(List[int(N/2)]-List[int((N/2)-1)])