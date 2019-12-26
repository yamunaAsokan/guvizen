n=int(input('enter the n th velue'))
sum=0
for i in range(2,n+1):
    for a in range(2,i):
        if(i%a)==0:
            break
    else:
        sum=sum+i
print(sum)
