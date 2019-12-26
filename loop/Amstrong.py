n=int(input('enter the number'))
temp=n
sum=0
while n>0:
    digit=n%10
    sum+=digit**3
    n=n//10
if(temp==sum):
        print('the number is amstrong')
else:
    print('the number is not amsstrong')
