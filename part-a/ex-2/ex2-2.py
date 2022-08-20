import math
n1=int(input('Enter first number in the range: '))
n2=int(input('Enter second number in the range: '))
for i in range(n1,n2+1):
    power=int(len(str(i))) # To find the number of digits in
    sum=0
    t=i
    while t!=0:
        d=t%10 # To separate individual digit
        sum=sum+math.pow(d,power)
        t=t//10
    if sum==i:
        print(i)
