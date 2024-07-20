# input a number and find if it is Prime number or not.
count=0
n=int(input('enter a number='))
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if(count==2):
    print('It is a Prime number')
else:
    print('It is not Prime number')
