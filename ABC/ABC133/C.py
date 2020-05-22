L,R=map(int, input().split())
ans=2019
for i in range(L,R+1):
    for j in range(L,R+1):
        if i==j:
            pass
        else:
            ans=min(ans,i*j%2019)
        if ans==0:
            print(ans)
            quit()
print(ans)