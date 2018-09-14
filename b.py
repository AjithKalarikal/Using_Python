print("enter the list of 5 numbers")
s=list()
for z in range(0,5):
    print("enter the number")
    print()
    s.append(int(input()))
for y in range(0,3):
    for x in range(0,4):
        if(s[x]>s[x+1]):
            s[x],s[x+1]=s[x+1],s[x]
for p in range(0,5):
    print(s[p],end=" ")
    
    
