A, B = map(int, input().split())
List=[]
List.append(A+B)
List.append(A-B)
List.append(A*B)
print(max(List))