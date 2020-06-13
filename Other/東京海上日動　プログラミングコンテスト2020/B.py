A,V=map(int, input().split())
B,W=map(int, input().split())
T=int(input())
if V<=W:
    print("NO")
    quit()
SA=abs(A-B)
CHIJI=(V-W)
SA=SA-(CHIJI*T)
if SA<=0:
    print("YES")
else:
    print("NO")