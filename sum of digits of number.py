#input a number and print sum of its digit.
print('input a number and print sum of its digits')
sum=0
n=int(input('enter any number='))
while(n>0):
    d=n%10
    sum=sum+d
    n=n//10
print('sum of digit=',sum)
