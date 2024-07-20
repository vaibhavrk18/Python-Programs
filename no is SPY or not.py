#input any number and check if it is Spy(SUM of no=PRODUCT of no) no or not.
sum=0
prod=1
n=int(input('enter any no='))
print('check if ',n,' is Spy no or not')
while(n>0):
    d=n%10
    sum=sum+d
    prod=prod*d
    n=n//10
print('sum of digits of no=',sum)
print('product of digits of no=',prod)
if(sum==prod):
    print('it is Spy no')
else:
    print('it is not Spy no')
