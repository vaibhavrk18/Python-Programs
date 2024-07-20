#print nos between a given range
print('enter nos between given range')
a=int(input('enter 1st no='))
b=int(input('enter 2nd no='))

if(a<b):
    i=a
    while(i<=b):
        print(i)
        i=i+1
elif(a>b):
    i=a
    while(i>=b):
        print(i)
        i=i-1
else:
    print('Both numbers are same')
    
