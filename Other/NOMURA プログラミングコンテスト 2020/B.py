S = list(input())
i=0
while i<len(S):
    if S[i]=="?":
        S[i]="D"
    i+=1
print("".join(S))