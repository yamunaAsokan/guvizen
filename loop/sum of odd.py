number=int(input('enter the n th number'))
sum=0
i=0
for i in range(1,number+1):
    if(i%2!=0):
        sum=sum+i
print('the sum is',sum) 
