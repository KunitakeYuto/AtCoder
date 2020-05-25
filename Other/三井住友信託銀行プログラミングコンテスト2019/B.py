import math
N=int(input())
i=1
while i<=N:
    if math.floor(i*1.08)==N:
        print(i)
        quit()
    i+=1
print(":(")