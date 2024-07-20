#print odd numbers between 30 to 50.
print('Print odd numbers between 30 to 50')
a=int(input('enter 1st no='))
b=int(input('enter 2nd no='))
if(a>=30) and (b<=50):
    print('Numbers are within the range')
    while(a<=b):
        print(a)
        a=a+1
print('END')
