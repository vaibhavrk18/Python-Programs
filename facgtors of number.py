# print factors of a number.
n=int(input('enter a number='))
print('Factors are:')
for i in range(1,n+1):
    if(n%i==0):
        print(i)
        i=i+1
print('END')
        
