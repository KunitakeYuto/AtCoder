n = int(input())
s = list(input())
 
for i in range(len(s)):
    s[i] = ord(s[i])+n
    if s[i] > 90:
        s[i] = chr(s[i]-26)
    else:
        s[i] = chr(s[i])
 
print("".join(s))