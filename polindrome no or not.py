# input a number and check if it is polindrome(original no = reverse no) no or not
print('check no is polindrome or not')
rev=0
n=int(input('enter any no='))
t=n
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
print('reverse of digits=',rev)
if(t==rev):
    print('it is a polindrome no')
else:
    print('it is not polindrome no')
