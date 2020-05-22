S=input()
a=0
b=0
c=0
i=0
while i<len(S):
    if S[i]=="a":
        a+=1
    elif S[i]=="b":
        b+=1
    else:
        c+=1
    i+=1
if a>b and a>c:
    print("a")
elif b>c:
    print("b")
else:
    print("c")