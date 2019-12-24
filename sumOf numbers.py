number=int(input('enter the n th number'))
sum=0
if(number>0):
    while(number>0):
        sum+=number
        number-=1
    print('the sum is',sum)
