number=int(input('enter the number'))
product=1
while(number>0):
    digit=number%10
    product=product*digit
    number=number//10
print('product of digits is:',product)
