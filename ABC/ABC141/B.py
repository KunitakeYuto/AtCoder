S=input()
i=0
while i<len(S):
    if (i+1)%2==0:
        if S[i]=="L" or S[i]=="U" or S[i]=="D":
            pass
        else:
            print("No")
            quit()
    else:
        if S[i]=="R" or S[i]=="U" or S[i]=="D":
            pass
        else:
            print("No")
            quit()
    i+=1
print("Yes")