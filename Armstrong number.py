#armstrong number=(whose sum of digits raised to the power of three equal the number itself
sum=0
n=int(input('enter any number='))
t=n

while(n>0):
    d=n%10
    cube=d**3
    sum=sum+cube
    n=n//10
print('sum of digits of number=',sum)
if(t==sum):
    print('number is Armstrong number')
else:
    print('number is not Armstrong number')
    
