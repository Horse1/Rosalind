s=str(input())
a=0
t=0
g=0
c=0
for i in range (0,len(s)):
    if s[i]=="A":
        a=a+1
for i in range (0,len(s)):
    if s[i]=="C":
        c=c+1
for i in range (0,len(s)):
    if s[i]=="G":
        g=g+1
for i in range (0,len(s)):
    if s[i]=="T":
        t=t+1
print (a,' ',c,' ',g,' ',t)        
