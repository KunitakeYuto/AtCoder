import math

N=int(input())

N2=int(math.sqrt(N))
mins=N-1

for i in range(1,N2+1):
    if N%i==0:
        mins=min(mins,(N//i-1)+(i-1))

print(mins)