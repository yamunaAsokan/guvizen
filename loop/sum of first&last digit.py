number=int(input('enter the number'))
number1=number%10
while(number>=10):
    number=number//10
print(number+number1)
