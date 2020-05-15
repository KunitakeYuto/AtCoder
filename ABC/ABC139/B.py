a, b = map(int, input().split())
if b==1:
    print(0)
    quit()
T=a
i=1
while 1==1:
    if T>=b:
        print(i)
        quit()
    T+=(a-1)
    i+=1