n=int(input('enter the input'))
a=1
if(n<0):
    print('not valid value')
elif(n==0):
        print('factorial of 0 is 1')
if(n>0):
    for i in range(1,n+1):
       a=a*i
    print('factorial of',n,'is',a)
