N=int(input())
i=1
j=1
while i<10:
    j=0
    while j<10:
        if j*i==N:
            print("Yes")
            quit()
        j+=1
    i+=1
print("No")