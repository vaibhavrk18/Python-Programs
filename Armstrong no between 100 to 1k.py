#print Armstrong number between 100 to 1000.
for i in range(100,1000):
    sum=0
    n=i
    while(n>0):
        d=n%10
        cube=d**3
        sum=sum+cube
        n=n//10
    if(i==sum):
        print('number is Armstrong number',sum)
print('END')
        
