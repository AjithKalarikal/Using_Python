
i=0
j=1
k=2
s=list()
sum=str()
sum1=str()
for x in range(0,12):
    print('Enter the number-')
    s.append(str(input()))
for y in range(0,4):
    sum=s[i]+s[j]+s[k]
    i=i+3
    j=j+3
    k=k+3
    sum1=sum[ : :-1]
    if(sum==sum1):
        print(sum)
        print(" is a pallindrome")
    else:
        print(sum)
        print(" is not  pallindrome")
    print()
        
    
