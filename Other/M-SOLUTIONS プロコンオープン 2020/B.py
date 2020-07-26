A,B,C = map(int, input().split())
K = int(input())
cnt=0
while 1:
    if not A<B:
        B=B*2
        cnt+=1
    else:
        break
    
while 1:
    if not B<C:
        C=C*2
        cnt+=1
    else:
        break
if cnt>K:
    print("No")
else:
    print("Yes")