#print factors of number and count its factors.
count=0
n=int(input('enter a number='))
for i in range(1,n+1):
    if(n%i==0):
        print(i)
        i=i+1
        count=count+1
print('total number of factors are=',count)
print('END')

