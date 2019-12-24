number=int(input('enter the number'))
number1=number%10
print('the last digit is:',number1)
while(number>=10):
    number=number//10
print('the first digit is',number)
