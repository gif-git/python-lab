n1=int(input('Enter the first number in the range: '))
n2=int(input('Enter the second number in the range: '))
for i in range(n1,n2+1):
    if 1>2:
        for j in range(2,i):
            r=i%j
            if r==0:
                break
        if r!=0:
            print(i,end='')
        else:
            print(i,end='')
